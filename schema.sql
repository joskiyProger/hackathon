--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: branches; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.branches (
    city character varying(30) NOT NULL,
    total_money numeric NOT NULL
);


ALTER TABLE public.branches OWNER TO postgres;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    id integer NOT NULL,
    uid character varying(50),
    surname character varying(25) NOT NULL,
    name character varying(25) NOT NULL,
    patronymic character varying(25),
    email character varying(100) NOT NULL,
    password character varying(50) NOT NULL,
    branch character varying(30) NOT NULL,
    total_money numeric NOT NULL
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- Name: employees_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.employees_id_seq OWNER TO postgres;

--
-- Name: employees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;


--
-- Name: transactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transactions (
    id integer NOT NULL,
    employee_id integer NOT NULL,
    money numeric NOT NULL,
    date_time timestamp without time zone NOT NULL
);


ALTER TABLE public.transactions OWNER TO postgres;

--
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transactions_id_seq OWNER TO postgres;

--
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transactions_id_seq OWNED BY public.transactions.id;


--
-- Name: employees id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);


--
-- Name: transactions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions ALTER COLUMN id SET DEFAULT nextval('public.transactions_id_seq'::regclass);


--
-- Name: branches branches_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.branches
    ADD CONSTRAINT branches_pkey PRIMARY KEY (city);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);


--
-- Name: employees fk_branch; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT fk_branch FOREIGN KEY (branch) REFERENCES public.branches(city);


--
-- Name: transactions fk_employee_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT fk_employee_id FOREIGN KEY (employee_id) REFERENCES public.employees(id);


--
-- PostgreSQL database dump complete
--

