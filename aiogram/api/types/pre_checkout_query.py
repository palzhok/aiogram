from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pydantic import Field

from .base import TelegramObject

if TYPE_CHECKING:
    from .order_info import OrderInfo
    from .user import User


class PreCheckoutQuery(TelegramObject):
    """
    This object contains information about an incoming pre-checkout query.

    Source: https://core.telegram.org/bots/api#precheckoutquery
    """

    id: str
    """Unique query identifier"""
    from_user: User = Field(..., alias="from")
    """User who sent the query"""
    currency: str
    """Three-letter ISO 4217 currency code"""
    total_amount: int
    """Total price in the smallest units of the currency (integer, not float/double). For example,
    for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it
    shows the number of digits past the decimal point for each currency (2 for the majority of
    currencies)."""
    invoice_payload: str
    """Bot specified invoice payload"""
    shipping_option_id: Optional[str] = None
    """Identifier of the shipping option chosen by the user"""
    order_info: Optional[OrderInfo] = None
    """Order info provided by the user"""