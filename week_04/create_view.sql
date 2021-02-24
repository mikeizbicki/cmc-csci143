CREATE VIEW payment_denormalized AS (
    SELECT
        amount,
        payment_date,
        return_date,
        rental_date,
        customer.first_name,
        customer.last_name,
        address,
        title,
        rating,
        length,
        name AS language,
        STRING_AGG(actor.first_name || ' ' || actor.last_name, ',')
    FROM payment
    INNER JOIN rental USING (rental_id)
    INNER JOIN inventory USING (inventory_id)
    INNER JOIN film USING (film_id)
    INNER JOIN language USING (language_id)
    INNER JOIN film_actor USING (film_id)
    INNER JOIN actor USING (actor_id)
    INNER JOIN customer ON customer.customer_id=payment.customer_id
    INNER JOIN address USING (address_id)
    GROUP BY 
        amount,
        payment_date,
        return_date,
        rental_date,
        title,
        rating,
        length,
        language,
        customer.first_name,
        customer.last_name,
        address
);
