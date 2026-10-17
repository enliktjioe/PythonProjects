/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

/*
 a.airplane_id as airplanes, 
 
 group by airline_id
 
 
select S.airline_id, S.airplane_id, ROUND(AVG(S.empty_seats),2) as avg_empty_seats

GROUP_CONCAT(S.airplane_id) as myList


    airlines_detail a
        join bookings b
        on a.airplane_id = b.airplane_id
    where (a.total_seats - b.booked) <= S2.avg_empty_seats + 1 
        OR (a.total_seats - b.booked) >= S2.avg_empty_seats - 1
    group by a.airline_id
*/


select *
    from
    (
        select S.airline_id, ROUND(AVG(S.empty_seats),2) as avg_empty_seats, COUNT(S.airplane_id), GROUP_CONCAT(S.airplane_id)
            from
            (
                select 
                    a.airline_id, 
                    a.airplane_id,
                    a.total_seats - b.booked as empty_seats
                    from airlines_detail a
                        join bookings b
                        on a.airplane_id = b.airplane_id
            ) S
        group by S.airline_id
        order by S.airline_id
    ) S2
;