import pytest
import asyncio

from app.data.event_bus import EventBus


class DummyEventA:
    pass


class DummyEventB:
    pass


@pytest.mark.asyncio
async def test_event_routing_success():
    bus = EventBus()

    received_a = []
    received_b = []

    def handle_a(event):
        received_a.append(event)

    async def handle_b(event):
        received_b.append(event)

    bus.subscribe(DummyEventA, handle_a)
    bus.subscribe(DummyEventB, handle_b)

    event_a = DummyEventA()
    event_b = DummyEventB()

    await bus.publish(event_a)
    assert len(received_a) == 1
    assert len(received_b) == 0

    await bus.publish(event_b)
    assert len(received_a) == 1
    assert len(received_b) == 1


@pytest.mark.asyncio
async def test_handler_error_isolation():
    bus = EventBus()

    received = []

    def bad_handler(event):
        raise ValueError("I failed")

    def good_handler(event):
        received.append(event)

    bus.subscribe(DummyEventA, bad_handler)
    bus.subscribe(DummyEventA, good_handler)

    event = DummyEventA()
    # Shouldn't raise the error, should be caught internally and good_handler still runs
    await bus.publish(event)

    assert len(received) == 1


@pytest.mark.asyncio
async def test_unsubscribe():
    bus = EventBus()
    received = []

    def handle_a(event):
        received.append(event)

    bus.subscribe(DummyEventA, handle_a)
    await bus.publish(DummyEventA())
    assert len(received) == 1

    bus.unsubscribe(DummyEventA, handle_a)
    await bus.publish(DummyEventA())
    # Shouldn't receive a second one
    assert len(received) == 1
