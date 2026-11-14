
"""Verifica a leitura completa de arquivos CSV com mais de 200 reservas."""

from helpers import run_cli


def test_processes_more_than_200_reservations(tmp_path):
    rows = [
        {
            "reservation_id": f"R-{i:03d}",
            "status": "CONFIRMED",
            "amount": "10.00",
        }
        for i in range(1, 251)
    ]

    report = run_cli(tmp_path, rows)

    assert report["summary"]["total_reservations"] == 250
    assert report["summary"]["confirmed_reservations"] == 250
    assert report["summary"]["total_room_nights"] == 250
    assert report["summary"]["total_amount_brl"] == "2500.00"
    assert report["by_month"][0]["reservations"] == 250
    assert report["top_hotels"][0]["total_brl"] == "2500.00"
