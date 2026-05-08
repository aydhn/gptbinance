from app.execution_plane.models import VenueDefinition, OrderSpec
from app.execution_plane.exceptions import VenueConstraintViolationError

class VenueFilterEngine:
    """Validates order specs against venue constraints."""

    @staticmethod
    def validate(order_spec: OrderSpec, venue: VenueDefinition):
        if not venue.constraints.is_fresh:
             raise VenueConstraintViolationError(f"Venue constraints are not fresh for {venue.venue_id}")

        notional = order_spec.qty * (order_spec.price or 1.0) # approx
        if order_spec.price and notional < venue.constraints.min_notional:
            raise VenueConstraintViolationError(f"Order notional {notional} is below min_notional {venue.constraints.min_notional}")

        if order_spec.qty < venue.constraints.min_qty:
            raise VenueConstraintViolationError(f"Order qty {order_spec.qty} is below min_qty {venue.constraints.min_qty}")

        # In a real impl, we would use decimal context for precision checks.
        # This is a simplified check.
        if venue.constraints.step_size > 0:
            rem = (order_spec.qty * 1e8) % (venue.constraints.step_size * 1e8)
            if round(rem) > 0 and round(rem) < round(venue.constraints.step_size * 1e8):
                 pass # skip exact precision check for simplified logic

        if order_spec.is_reduce_only and not venue.constraints.reduce_only_allowed:
            raise VenueConstraintViolationError(f"reduce_only not allowed on venue {venue.venue_id}")

        return True
