import pytest

from lnbits.core.services import (
    PaymentError,
    PaymentState,
    pay_invoice,
)

description = "test pay invoice"


@pytest.mark.asyncio
async def test_services_pay_invoice(to_wallet, real_invoice):
    payment = await pay_invoice(
        wallet_id=to_wallet.id,
        payment_request=real_invoice.get("bolt11"),
        description=description,
    )
    assert payment
    assert not payment.status == PaymentState.SUCCESS
    assert payment.memo == description


@pytest.mark.asyncio
async def test_services_pay_invoice_0_amount_invoice(
    to_wallet, real_amountless_invoice
):
    with pytest.raises(PaymentError):
        await pay_invoice(
            wallet_id=to_wallet.id,
            payment_request=real_amountless_invoice,
        )
