PGDMP     .    "        
    
    y           taller3    14.0    14.0 $               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    40960    taller3    DATABASE     c   CREATE DATABASE taller3 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Chile.1252';
    DROP DATABASE taller3;
                postgres    false            �            1259    41011    ataque    TABLE     �   CREATE TABLE public.ataque (
    id integer NOT NULL,
    tipo_at character varying(50) NOT NULL,
    "daño_base" integer NOT NULL
);
    DROP TABLE public.ataque;
       public         heap    postgres    false            �            1259    41010    ataque_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ataque_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.ataque_id_seq;
       public          postgres    false    212                       0    0    ataque_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.ataque_id_seq OWNED BY public.ataque.id;
          public          postgres    false    211            �            1259    41004 
   entrenador    TABLE     �   CREATE TABLE public.entrenador (
    id integer NOT NULL,
    nombre character varying(50),
    password character varying(50),
    nombre_usuario character varying(50),
    fecha_nac date,
    edad integer
);
    DROP TABLE public.entrenador;
       public         heap    postgres    false            �            1259    41003    entrenador_id_seq    SEQUENCE     �   CREATE SEQUENCE public.entrenador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.entrenador_id_seq;
       public          postgres    false    210                       0    0    entrenador_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.entrenador_id_seq OWNED BY public.entrenador.id;
          public          postgres    false    209            �            1259    41022    especie    TABLE     �   CREATE TABLE public.especie (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    id_tipo integer,
    id_tipo2 integer
);
    DROP TABLE public.especie;
       public         heap    postgres    false            �            1259    41057    estadisticas    TABLE     �   CREATE TABLE public.estadisticas (
    id integer NOT NULL,
    nombre_combate character varying(50),
    ganado boolean,
    perdido boolean,
    id_user integer
);
     DROP TABLE public.estadisticas;
       public         heap    postgres    false            �            1259    41037 	   monstruos    TABLE       CREATE TABLE public.monstruos (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    velocidad integer NOT NULL,
    salud integer NOT NULL,
    id_user integer NOT NULL,
    id_ataque integer NOT NULL,
    id_especie integer NOT NULL
);
    DROP TABLE public.monstruos;
       public         heap    postgres    false            �            1259    41017    tipos    TABLE     �   CREATE TABLE public.tipos (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    fortaleza character varying(50),
    debilidad character varying(50)
);
    DROP TABLE public.tipos;
       public         heap    postgres    false            r           2604    41014 	   ataque id    DEFAULT     f   ALTER TABLE ONLY public.ataque ALTER COLUMN id SET DEFAULT nextval('public.ataque_id_seq'::regclass);
 8   ALTER TABLE public.ataque ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211    212            q           2604    41007    entrenador id    DEFAULT     n   ALTER TABLE ONLY public.entrenador ALTER COLUMN id SET DEFAULT nextval('public.entrenador_id_seq'::regclass);
 <   ALTER TABLE public.entrenador ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210                      0    41011    ataque 
   TABLE DATA           ;   COPY public.ataque (id, tipo_at, "daño_base") FROM stdin;
    public          postgres    false    212   �(                 0    41004 
   entrenador 
   TABLE DATA           [   COPY public.entrenador (id, nombre, password, nombre_usuario, fecha_nac, edad) FROM stdin;
    public          postgres    false    210   \)                 0    41022    especie 
   TABLE DATA           @   COPY public.especie (id, nombre, id_tipo, id_tipo2) FROM stdin;
    public          postgres    false    214   �)                 0    41057    estadisticas 
   TABLE DATA           T   COPY public.estadisticas (id, nombre_combate, ganado, perdido, id_user) FROM stdin;
    public          postgres    false    216   7*                 0    41037 	   monstruos 
   TABLE DATA           a   COPY public.monstruos (id, nombre, velocidad, salud, id_user, id_ataque, id_especie) FROM stdin;
    public          postgres    false    215   T*                 0    41017    tipos 
   TABLE DATA           A   COPY public.tipos (id, nombre, fortaleza, debilidad) FROM stdin;
    public          postgres    false    213   q*                   0    0    ataque_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.ataque_id_seq', 6, true);
          public          postgres    false    211            !           0    0    entrenador_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.entrenador_id_seq', 4, true);
          public          postgres    false    209            v           2606    41016    ataque ataque_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.ataque
    ADD CONSTRAINT ataque_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.ataque DROP CONSTRAINT ataque_pkey;
       public            postgres    false    212            t           2606    41009    entrenador entrenador_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.entrenador
    ADD CONSTRAINT entrenador_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.entrenador DROP CONSTRAINT entrenador_pkey;
       public            postgres    false    210            z           2606    41026    especie especie_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.especie
    ADD CONSTRAINT especie_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.especie DROP CONSTRAINT especie_pkey;
       public            postgres    false    214            ~           2606    41061    estadisticas estadisticas_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.estadisticas
    ADD CONSTRAINT estadisticas_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.estadisticas DROP CONSTRAINT estadisticas_pkey;
       public            postgres    false    216            |           2606    41041    monstruos monstruos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.monstruos
    ADD CONSTRAINT monstruos_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.monstruos DROP CONSTRAINT monstruos_pkey;
       public            postgres    false    215            x           2606    41021    tipos tipos_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.tipos
    ADD CONSTRAINT tipos_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.tipos DROP CONSTRAINT tipos_pkey;
       public            postgres    false    213            �           2606    41032    especie especie_id_tipo2_fkey    FK CONSTRAINT     }   ALTER TABLE ONLY public.especie
    ADD CONSTRAINT especie_id_tipo2_fkey FOREIGN KEY (id_tipo2) REFERENCES public.tipos(id);
 G   ALTER TABLE ONLY public.especie DROP CONSTRAINT especie_id_tipo2_fkey;
       public          postgres    false    213    214    3192                       2606    41027    especie especie_id_tipo_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.especie
    ADD CONSTRAINT especie_id_tipo_fkey FOREIGN KEY (id_tipo) REFERENCES public.tipos(id);
 F   ALTER TABLE ONLY public.especie DROP CONSTRAINT especie_id_tipo_fkey;
       public          postgres    false    3192    213    214            �           2606    41062 &   estadisticas estadisticas_id_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.estadisticas
    ADD CONSTRAINT estadisticas_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.entrenador(id);
 P   ALTER TABLE ONLY public.estadisticas DROP CONSTRAINT estadisticas_id_user_fkey;
       public          postgres    false    210    3188    216            �           2606    41047 "   monstruos monstruos_id_ataque_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.monstruos
    ADD CONSTRAINT monstruos_id_ataque_fkey FOREIGN KEY (id_ataque) REFERENCES public.ataque(id);
 L   ALTER TABLE ONLY public.monstruos DROP CONSTRAINT monstruos_id_ataque_fkey;
       public          postgres    false    212    215    3190            �           2606    41052 #   monstruos monstruos_id_especie_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.monstruos
    ADD CONSTRAINT monstruos_id_especie_fkey FOREIGN KEY (id_especie) REFERENCES public.especie(id);
 M   ALTER TABLE ONLY public.monstruos DROP CONSTRAINT monstruos_id_especie_fkey;
       public          postgres    false    3194    214    215            �           2606    41042     monstruos monstruos_id_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.monstruos
    ADD CONSTRAINT monstruos_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.entrenador(id);
 J   ALTER TABLE ONLY public.monstruos DROP CONSTRAINT monstruos_id_user_fkey;
       public          postgres    false    3188    215    210               Q   x���� ��n1P{�s!g$AQ����wKϛb�7��o<�p�D���A��^�d==z�Z�ʀ]�.�̆�@���         ^   x�-�Q
�  ���.F��ݠ	�2����?��J��Z;<wj��Fv���Kl�* lBL��|*a%b���R�Q��Lj<�"��%         ]   x�%�=@@��Fb���P�l�	��<������L�k�y^3,|G
��rpZ���#�6ǉo�M#�s�\),����Ua������WD�y��            x������ � �            x������ � �         j   x�M�K
�0Dי��=��P��jm�/���$�y��v�=Z�h�fb�(�5��X��P�d��{T�x�_���)���T��4D�c�12�{%��g N�t@z     