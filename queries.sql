-- 2.1 Все поля всех фильмов
SELECT * FROM films;

-- 2.2 Название и режиссёр
SELECT Название, Режиссёр FROM films;

-- 2.3 Название, режиссёр, год
SELECT Название, Режиссёр, Год FROM films;

-- 2.4 Фильмы Нолана
SELECT * FROM films WHERE Режиссёр = 'Нолан';

-- 2.5 Фильмы 2009 года
SELECT * FROM films WHERE Год = 2009;

-- 2.6 Фильмы до 2000 года
SELECT * FROM films WHERE Год < 2000;

-- 2.7 Фильмы после 2010 года
SELECT * FROM films WHERE Год > 2010;

-- 2.8 Фильмы длиннее 140 минут
SELECT * FROM films WHERE Минуты > 140;

-- 2.9 Фильмы 120 минут и дольше
SELECT * FROM films WHERE Минуты >= 120;

-- 2.10 Фильмы любимого режиссёра (Нолан)
SELECT * FROM films WHERE Режиссёр = 'Нолан';

-- 2.11 Сортировка по названию
SELECT * FROM films ORDER BY Название ASC;