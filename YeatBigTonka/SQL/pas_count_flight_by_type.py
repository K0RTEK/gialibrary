def sql():
    a = """
        SELECT
            p.name,
            t.plane,
            COUNT(*) AS cnt_trip
        FROM Passenger p
        JOIN Pass_in_trip pt ON p.ID_psg = pt.ID_psg
        JOIN Trip t ON pt.trip_no = t.trip_no
        GROUP BY p.ID_psg, p.name, t.plane
        ORDER BY p.name, cnt_trip DESC;
    """