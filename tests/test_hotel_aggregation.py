
"""Testa acumulação por hotel, desempate e limite do ranking."""

from helpers import run_cli


def test_hotel_aggregation_and_tie_break_by_id(tmp_path):
    """Soma reservas por hotel e desempata pelo ID em ordem crescente."""
    report = run_cli(
        tmp_path,
        [
            {"reservation_id": "R-1", "hotel_id": "H02", "hotel_name": "Hotel B", "amount": "900.00"},
            {"reservation_id": "R-2", "hotel_id": "H01", "hotel_name": "Hotel A", "amount": "300.00"},
            {"reservation_id": "R-3", "hotel_id": "H04", "hotel_name": "Hotel D", "amount": "100.00"},
            {"reservation_id": "R-4", "hotel_id": "H03", "hotel_name": "Hotel C", "amount": "1200.00"},
            {
                "reservation_id": "R-5",
                "hotel_id": "H01",
                "hotel_name": "Hotel A",
                "checkout_date": "2025-01-12",
                "amount": "600.00",
            },
        ],
        top=3,
    )

    assert report["top_hotels"] == [
        {"hotel_id": "H03", "hotel_name": "Hotel C", "room_nights": 1, "total_brl": "1200.00"},
        {"hotel_id": "H01", "hotel_name": "Hotel A", "room_nights": 3, "total_brl": "900.00"},
        {"hotel_id": "H02", "hotel_name": "Hotel B", "room_nights": 1, "total_brl": "900.00"},
    ]
    assert report["summary"]["total_amount_brl"] == "3100.00"
