-- Использованный запрос в PostgreSQL для создания базы данных
-- Удаление существующих таблиц, если они есть
DROP TABLE IF EXISTS "public"."pereval_images" CASCADE;
DROP TABLE IF EXISTS "public"."pereval_added" CASCADE;
DROP TABLE IF EXISTS "public"."coords" CASCADE;
DROP TABLE IF EXISTS "public"."users" CASCADE;
DROP TABLE IF EXISTS "public"."spr_activities_types" CASCADE;

-- Определение последовательностей
CREATE SEQUENCE IF NOT EXISTS USER_ID_SEQ;
CREATE SEQUENCE IF NOT EXISTS COORDS_ID_SEQ;
CREATE SEQUENCE IF NOT EXISTS PEREVAL_ID_SEQ;
CREATE SEQUENCE IF NOT EXISTS IMAGE_ID_SEQ;

-- Таблица для пользователей
CREATE TABLE "public"."users" (
    "id" INT4 NOT NULL DEFAULT NEXTVAL('USER_ID_SEQ'::REGCLASS),
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "fam" TEXT,
    "name" TEXT,
    "otc" TEXT,
    "phone" TEXT,
    PRIMARY KEY ("id")
);

-- Таблица для координат
CREATE TABLE "public"."coords" (
    "id" INT4 NOT NULL DEFAULT NEXTVAL('COORDS_ID_SEQ'::REGCLASS),
    "latitude" FLOAT8 NOT NULL,
    "longitude" FLOAT8 NOT NULL,
    "height" INT4 NOT NULL,
    PRIMARY KEY ("id")
);

-- Таблица для перевалов
CREATE TABLE "public"."pereval_added" (
    "id" INT4 NOT NULL DEFAULT NEXTVAL('PEREVAL_ID_SEQ'::REGCLASS),
    "beauty_title" TEXT,
    "title" TEXT,
    "other_titles" TEXT,
    "connect" TEXT,
    "add_time" TIMESTAMP,
    "user_id" INT4 REFERENCES "public"."users"("id"),
    "coord_id" INT4 REFERENCES "public"."coords"("id"),
    "level_winter" TEXT,
    "level_summer" TEXT,
    "level_autumn" TEXT,
    "level_spring" TEXT,
    "status" TEXT DEFAULT 'new' CHECK (status IN ('new', 'pending', 'accepted', 'rejected')),
    PRIMARY KEY ("id")
);

-- Таблица для изображений
CREATE TABLE "public"."pereval_images" (
    "id" INT4 NOT NULL DEFAULT NEXTVAL('IMAGE_ID_SEQ'::REGCLASS),
    "pereval_id" INT4 REFERENCES "public"."pereval_added"("id"),
    "title" TEXT,
    "img" BYTEA NOT NULL,
    PRIMARY KEY ("id")
);

-- Таблица для типов активности
CREATE SEQUENCE IF NOT EXISTS UNTITLED_TABLE_200_ID_SEQ;
CREATE TABLE "public"."spr_activities_types" (
    "id" INT4 NOT NULL DEFAULT NEXTVAL('UNTITLED_TABLE_200_ID_SEQ'::REGCLASS),
    "title" TEXT,
    PRIMARY KEY ("id")
);