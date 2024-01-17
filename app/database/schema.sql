--
-- PostgreSQL database dump
--

-- Dumped from database version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- Name: league_type; Type: TYPE; Schema: public; Owner: reniel
--

CREATE TYPE public.league_type AS ENUM (
    'league',
    'cup',
    'super-cup'
);


ALTER TYPE public.league_type OWNER TO reniel;

--
-- Name: sport_type; Type: TYPE; Schema: public; Owner: reniel
--

CREATE TYPE public.sport_type AS ENUM (
    'Soccer',
    'Basketball',
    'Football',
    'Baseball',
    'Cricket',
    'Rugby',
    'Hockey',
    'Volleyball',
    'Handball',
    'Softball'
);


ALTER TYPE public.sport_type OWNER TO reniel;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: countries; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.countries (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    code character(2) NOT NULL,
    name character varying(55) NOT NULL
);


ALTER TABLE public.countries OWNER TO reniel;

--
-- Name: fixtures; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.fixtures (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    id integer NOT NULL,
    sport public.sport_type NOT NULL,
    home_team_id uuid NOT NULL,
    away_team_id uuid NOT NULL,
    venue_id uuid NOT NULL,
    "timestamp" timestamp without time zone,
    is_finished boolean DEFAULT false NOT NULL,
    is_home_team_home boolean DEFAULT true NOT NULL
);


ALTER TABLE public.fixtures OWNER TO reniel;

--
-- Name: leagues; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.leagues (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    sport public.sport_type NOT NULL,
    country_id uuid NOT NULL,
    type public.league_type NOT NULL
);


ALTER TABLE public.leagues OWNER TO reniel;

--
-- Name: seasons; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.seasons (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    id integer NOT NULL,
    league_id uuid NOT NULL,
    sport public.sport_type NOT NULL,
    year integer NOT NULL,
    start date NOT NULL,
    "end" date NOT NULL
);


ALTER TABLE public.seasons OWNER TO reniel;

--
-- Name: teams; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.teams (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    id integer NOT NULL,
    name character varying(55) NOT NULL,
    code character(3) NOT NULL,
    sport public.sport_type NOT NULL,
    home_venue_id uuid NOT NULL
);


ALTER TABLE public.teams OWNER TO reniel;

--
-- Name: venues; Type: TABLE; Schema: public; Owner: reniel
--

CREATE TABLE public.venues (
    uuid uuid DEFAULT gen_random_uuid() NOT NULL,
    id integer NOT NULL,
    name character varying(55),
    city_name character varying(55)
);


ALTER TABLE public.venues OWNER TO reniel;

--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (uuid);


--
-- Name: fixtures fixtures_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.fixtures
    ADD CONSTRAINT fixtures_pkey PRIMARY KEY (uuid);


--
-- Name: leagues leagues_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.leagues
    ADD CONSTRAINT leagues_pkey PRIMARY KEY (uuid);


--
-- Name: seasons seasons_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.seasons
    ADD CONSTRAINT seasons_pkey PRIMARY KEY (uuid);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (uuid);


--
-- Name: venues venues_pkey; Type: CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.venues
    ADD CONSTRAINT venues_pkey PRIMARY KEY (uuid);


--
-- Name: fixtures fixtures_away_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.fixtures
    ADD CONSTRAINT fixtures_away_team_id_fkey FOREIGN KEY (away_team_id) REFERENCES public.teams(uuid);


--
-- Name: fixtures fixtures_home_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.fixtures
    ADD CONSTRAINT fixtures_home_team_id_fkey FOREIGN KEY (home_team_id) REFERENCES public.teams(uuid);


--
-- Name: fixtures fixtures_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.fixtures
    ADD CONSTRAINT fixtures_venue_id_fkey FOREIGN KEY (venue_id) REFERENCES public.venues(uuid);


--
-- Name: leagues leagues_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.leagues
    ADD CONSTRAINT leagues_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(uuid);


--
-- Name: seasons seasons_league_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.seasons
    ADD CONSTRAINT seasons_league_id_fkey FOREIGN KEY (league_id) REFERENCES public.leagues(uuid);


--
-- Name: teams teams_home_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: reniel
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_home_venue_id_fkey FOREIGN KEY (home_venue_id) REFERENCES public.venues(uuid);


--
-- PostgreSQL database dump complete
--

