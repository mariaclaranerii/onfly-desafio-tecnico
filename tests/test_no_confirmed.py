
"""Valida o relatório quando não há reservas confirmadas."""

from helpers import run_cli


def test_no_confirmed_reservations_have_zero_totals_and_empty_groups(tmp_path):
    """Conta reservas não faturáveis, mas não gera noites, valores ou agregações."""
    rows = [
        {
            "reservation_id": "R-1",
            "status": "CANCELLED",
            "amount": "9999.00",
            "currency": "USD",
            "hotel_id": "H01",
            "checkin_date": "2025-01-10",
            "checkout_date": "2025-01-11",
        },
        {
            "reservation_id": "R-2",
            "status": "NO_SHOW",
            "amount": "8888.00",
            "currency": "EUR",
            "hotel_id": "H02",
            "checkin_date": "2025-02-10",
            "checkout_date": "2025-02-11",
        },
        {
            "reservation_id": "R-3",
            "status": "CANCELLED",
            "amount": "7777.00",
            "currency": "BRL",
            "hotel_id": "H03",
            "checkin_date": "2025-03-10",
            "checkout_date": "2025-03-11",
        },
    ]

    report = run_cli(tmp_path, rows)

    assert report["summary"] == {
        "total_reservations": 3,
        "confirmed_reservations": 0,
        "cancelled_reservations": 2,
        "no_show_reservations": 1,
        "total_room_nights": 0,
        "total_amount_brl": "0.00",
        "average_nightly_rate_brl": "0.00",
    }
    assert report["by_month"] == []
    assert report["top_hotels"] == []
