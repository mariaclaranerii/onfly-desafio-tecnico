
"""Verifica precisão Decimal e arredondamento somente no relatório."""

from helpers import run_cli


def test_money_precision_sums_before_rounding(tmp_path):
    """Soma conversões exatas antes de aplicar ROUND_HALF_UP."""
    report = run_cli(
        tmp_path,
        [
            {"reservation_id": "R-1", "currency": "USD", "amount": "0.75"},
            {"reservation_id": "R-2", "currency": "USD", "amount": "0.75"},
        ],
    )

    summary = report["summary"]
    assert summary["total_room_nights"] == 2
    assert summary["total_amount_brl"] == "8.13"
    assert summary["average_nightly_rate_brl"] == "4.07"

    assert report["by_month"][0]["total_brl"] == "8.13"
    assert report["top_hotels"][0]["total_brl"] == "8.13"
