from app.order_lifecycle.models import VenueAck, VenueReject, PartialFill, FullFill


class VenueEventMapper:
    def map_ack(self, payload: dict) -> VenueAck:
        pass

    def map_reject(self, payload: dict) -> VenueReject:
        pass
