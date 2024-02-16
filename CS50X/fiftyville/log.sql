-- Select all reports from Humphrey Street where "CS50 duck" is mentioned.
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND description LIKE '%CS50 duck%';
-- +-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | id  | year | month | day |     street      |                                                                                                       description                                                                                                        |
-- +-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
-- +-----+------+-------+-----+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-- Select all interviews from the date of the crime where "bakery" is mentioned.
SELECT * FROM interviews WHERE month = '7' AND day = '28' AND transcript LIKE '%bakery%';
-- +-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
-- +-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
-- +-----+---------+------+-------+-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-- Select all security logs from that specific time of the crime (+ 10 minutes) where someone exited the bakery.
SELECT * FROM bakery_security_logs WHERE year = '2021' AND month = '7' AND day = '28' AND hour = '10' AND minute <= '25' AND minute >= '15' AND activity = 'exit';
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | id  | year | month | day | hour | minute | activity | license_plate |
-- +-----+------+-------+-----+------+--------+----------+---------------+
-- | 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
-- | 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
-- | 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
-- | 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
-- | 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
-- | 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
-- | 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
-- | 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
-- +-----+------+-------+-----+------+--------+----------+---------------+

-- Select all phone calls from the day of the crime with a duration of less than 1 minute (just like the witness stated).
SELECT * FROM phone_calls WHERE year = '2021' AND month = '7' AND day = '28' AND duration <= '60';
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
-- | 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- | 234 | (609) 555-5876 | (389) 555-5198 | 2021 | 7     | 28  | 60       |
-- | 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
-- | 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
-- | 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
-- | 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
-- | 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |
-- +-----+----------------+----------------+------+-------+-----+----------+

-- Select all ATM transactions from the time where the witness saw the suspect withdrawing money.
SELECT * FROM atm_transactions WHERE year = '2021' AND month = '7' AND day = '28' AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+
-- | 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
-- | 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
-- | 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
-- | 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
-- | 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+

-- Filter all bank accounts that were involved in transactions witnessed at the ATM. The owner of one of these bank accounts is the thief.
SELECT * FROM bank_accounts WHERE account_number IN ('28500762', '28296815', '76054385', '49610011', '16153065', '25506511', '81061156', '26013199');
-- +----------------+-----------+---------------+
-- | account_number | person_id | creation_year |
-- +----------------+-----------+---------------+
-- | 49610011       | 686048    | 2010          |
-- | 26013199       | 514354    | 2012          |
-- | 16153065       | 458378    | 2012          |
-- | 28296815       | 395717    | 2014          |
-- | 25506511       | 396669    | 2014          |
-- | 28500762       | 467400    | 2014          |
-- | 76054385       | 449774    | 2015          |
-- | 81061156       | 438727    | 2018          |
-- +----------------+-----------+---------------+

-- Filter people by involved licence plates and ids from bank accounts. One of these people has to be the thief.
SELECT * FROM people WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE', '0NTHK55') AND id IN ('686048', '514354', '458378', '395717', '396669', '467400', '449774', '438727');
-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+-------+----------------+-----------------+---------------+

-- Filter calls by suspects. Considering the results (by looking at the phone numbers), Bruce or Diana has to be the thief.
SELECT * FROM phone_calls WHERE year = '2021' AND month = '7' AND day = '28' AND duration <= '60' AND caller IN ('(829) 555-5269', '(389) 555-5198', '(770) 555-1861', '(367) 555-5533');
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
-- +-----+----------------+----------------+------+-------+-----+----------+

-- Find out the ID of the Fiftyville Airport
SELECT * FROM airports WHERE city = 'Fiftyville';
-- +----+--------------+-----------------------------+------------+
-- | id | abbreviation |          full_name          |    city    |
-- +----+--------------+-----------------------------+------------+
-- | 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
-- +----+--------------+-----------------------------+------------+

-- Select the first flight from the Fiftyville airport the day after the incident (like the witness heard the suspect saying on the phone).
SELECT * FROM flights WHERE origin_airport_id = '8' AND year = '2021' AND month = '7' AND day = '29' ORDER BY hour LIMIT 1;
-- +----+-------------------+------------------------+------+-------+-----+------+--------+
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+

-- Find the destination airport.
SELECT * FROM airports WHERE id = '4';
-- +----+--------------+-------------------+---------------+
-- | id | abbreviation |     full_name     |     city      |
-- +----+--------------+-------------------+---------------+
-- | 4  | LGA          | LaGuardia Airport | New York City |
-- +----+--------------+-------------------+---------------+

-- Filter the passengers of the flight by the passport numbers of Bruce and Diana. If only one result comes up, its the thief.
SELECT * FROM passengers WHERE flight_id = '36' AND passport_number IN ('7049073643', '8496433585', '3592750733', '5773159633');
-- +-----------+-----------------+------+
-- | flight_id | passport_number | seat |
-- +-----------+-----------------+------+
-- | 36        | 5773159633      | 4A   |
-- +-----------+-----------------+------+

-- Get the thieves name - it's Bruce.
SELECT * FROM people WHERE passport_number = '5773159633';
-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- +--------+-------+----------------+-----------------+---------------+

-- Find out who Bruce called.
SELECT * FROM phone_calls WHERE year = '2021' AND month = '7' AND day = '28' AND duration <= '60' AND caller = '(367) 555-5533';
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- +-----+----------------+----------------+------+-------+-----+----------+

-- Get the accomplices clear name.
SELECT * FROM people WHERE phone_number = '(375) 555-8161';
-- +--------+-------+----------------+-----------------+---------------+
-- |   id   | name  |  phone_number  | passport_number | license_plate |
-- +--------+-------+----------------+-----------------+---------------+
-- | 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
-- +--------+-------+----------------+-----------------+---------------+