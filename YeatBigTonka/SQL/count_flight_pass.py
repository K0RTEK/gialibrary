def sql():
    a = """
        SELECT 
            t.trip_no,
            c.name AS name,
            t.town_from,
            t.town_to,
            COUNT(DISTINCT pt.date_trip) AS cnt_trip,
            COUNT(*) AS cnt_psg
        FROM Trip t
        JOIN Company c ON t.ID_comp = c.ID_comp
        JOIN Pass_in_trip pt ON t.trip_no = pt.trip_no
        GROUP BY t.trip_no, c.name, t.town_from, t.town_to
        ORDER BY t.trip_no;


    """