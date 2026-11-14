
"""Testa o agrupamento mensal pelo mês do check-in."""

from helpers import run_cli


def test_monthly_aggregation_uses_checkin_and_excludes_non_billable(tmp_path):
    """Agrupa, acumula e ordena apenas reservas confirmadas pelo check-in."""
    rows = [
        {
            "reservation_id": "R-1",
            "checkin_date": "2025-02-10",
            "checkout_date": "2025-02-12",
            "amount": "200.00",
        },
        {
            "reservation_id": "R-2",
            "checkin_date": "2025-01-30",
            "checkout_date": "2025-02-02",
            "rooms": "2",
            "amount": "300.00",
        },
        {
            "reservation_id": "R-3",
            "checkin_date": "2024-12-31",
            "checkout_date": "2025-01-02",
            "amount": "100.00",
        },
        {
            "reservation_id": "R-4",
            "checkin_date": "2025-01-05",
            "checkout_date": "2025-01-06",
            "amount": "150.00",
        },
        {
            "reservation_id": "R-5",
            "checkin_date": "2025-03-10",
            "checkout_date": "2025-03-11",
            "status": "CANCELLED",
            "amount": "10000.00",
        },
        {
            "reservation_id": "R-6",
            "checkin_date": "2025-02-25",
            "checkout_date": "2025-02-26",
            "status": "NO_SHOW",
            "amount": "10000.00",
        },
    ]

    report = run_cli(tmp_path, rows)

    assert report["by_month"] == [
        {"month": "2024-12", "reservations": 1, "room_nights": 2, "total_brl": "100.00"},
        {"month": "2025-01", "reservations": 2, "room_nights": 7, "total_brl": "450.00"},
        {"month": "2025-02", "reservations": 1, "room_nights": 2, "total_brl": "200.00"},
    ]
