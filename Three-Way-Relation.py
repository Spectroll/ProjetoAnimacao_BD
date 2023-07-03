from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

#Bloco para a entidade Distribuição:
#---------------------------------------------------------------------------------------------------------------------------------------#
distribuition_title = Text("Distribution", color = BLACK, font_size= 24)
distribuition_shape = SurroundingRectangle(distribuition_title, color = BLACK, buff = 0.4)
distribuition_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(distribuition_shape.get_bottom(), DOWN).shift(LEFT)
distribuition_att_date = Tex("Starting Date", color= BLACK, font_size= 20).next_to(distribuition_att, DOWN, buff= 0.05)
distribuition_att_con = Line(start= [-1, -0.55, 0], end= distribuition_att.get_top(), color= BLACK)

distribuition = VGroup(distribuition_title, distribuition_shape, distribuition_att, distribuition_att_con, distribuition_att_date)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Distribuidor:
#---------------------------------------------------------------------------------------------------------------------------------------#
dist_title = Text("Distributor", color = BLACK, font_size= 24)
dist_shape = SurroundingRectangle(dist_title, color = BLACK, buff = 0.4)
dist_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(dist_shape.get_bottom(), DOWN).shift(RIGHT*0.5)
dist_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(dist_shape.get_bottom(), DOWN).shift(RIGHT).shift(DOWN*0.2)
dist_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(dist_att, DOWN, buff= 0.05)
dist_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(dist_att2, DOWN, buff= 0.05)
dist_att_con = Line(start= [0.5, -0.55, 0], end= dist_att.get_top(), color= BLACK)
dist_att_con2 = Line(start= [1, -0.55, 0], end= dist_att2.get_top(), color= BLACK)

dist = VGroup(dist_title, dist_shape, dist_att, dist_att_code, dist_att_con, dist_att2, dist_att_name, dist_att_con2).next_to(distribuition, UR*2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Cidade:
#---------------------------------------------------------------------------------------------------------------------------------------#
city_title = Text("City", color = BLACK, font_size= 24)
city_shape = dist_shape.copy().next_to(city_title.get_left()).shift(LEFT*1.21)
city_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(city_shape.get_bottom(), DOWN).shift(LEFT).shift(DOWN*0.2)
city_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(city_shape.get_bottom(), DOWN).shift(LEFT*0.5)
city_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(city_att, DOWN, buff= 0.05)
city_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(city_att2, DOWN, buff= 0.05)
city_att_con = Line(start= [-1, -0.55, 0], end= city_att.get_top(), color= BLACK)
city_att_con2 = Line(start= [-0.5, -0.55, 0], end= city_att2.get_top(), color= BLACK)

city = VGroup(city_title, city_shape, city_att, city_att_code, city_att_con, city_att2, city_att_name, city_att_con2).next_to(distribuition, UL*2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Produto:
#---------------------------------------------------------------------------------------------------------------------------------------#
prod_title = Text("Product", color = BLACK, font_size= 24)
prod_shape = SurroundingRectangle(prod_title, color = BLACK, buff = 0.4)
prod_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(prod_shape.get_bottom(), DL*1.5)
prod_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(prod_shape.get_bottom(), DOWN)
prod_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(prod_att, DOWN, buff= 0.05)
prod_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(prod_att2, DOWN, buff= 0.05)
prod_att_con = Line(start= [-0.475, -0.55, 0], end= prod_att.get_top(), color= BLACK)
prod_att_con2 = Line(start= prod_shape.get_bottom(), end= prod_att2.get_top(), color= BLACK)

prod = VGroup(prod_title, prod_shape, prod_att, prod_att_code, prod_att_con, prod_att2, prod_att_name, prod_att_con2).next_to(distribuition, DOWN*3).shift(RIGHT*0.15)
#---------------------------------------------------------------------------------------------------------------------------------------#


#Relacoes entre os blocos
#---------------------------------------------------------------------------------------------------------------------------------------#
distr_prod = Line(distribuition_shape.get_bottom(), prod_shape.get_top(), color= BLACK)
p1 = Point(city_shape.get_bottom()).shift(RIGHT*0.25)
p2 = Point(distribuition_shape.get_top()).shift(LEFT*0.25)
distr_city = Line(p1, p2, color= BLACK)
p3 = Point(dist_shape.get_bottom()).shift(LEFT*0.25)
p4 = Point(distribuition_shape.get_top()).shift(RIGHT*0.25)
distr_dist = Line(p3, p4, color= BLACK)

relation_connectors = VGroup(distr_prod, distr_city, distr_dist)

city_distr_cardi = Tex(r'\textbf{(1, 1)}', color= BLACK, font_size= 26).next_to(distr_city.get_start(), DOWN, buff=0.1).shift(RIGHT*1.2)
distr_city_cardi = Tex(r'\textbf{(0, N)}', color= BLACK, font_size= 26).next_to(distr_city.get_end(), UP, buff=0.3).shift(LEFT*0.25)
dist_distr_cardi = Tex(r'\textbf{(1, 1)}', color= BLACK, font_size= 26).next_to(distr_dist.get_start(), DOWN, buff=0.1).shift(LEFT*1.2)
distr_dist_cardi = Tex(r'\textbf{(0, N)}', color= BLACK, font_size= 26).next_to(distr_dist.get_end(), UP, buff=0.3).shift(RIGHT*0.2)
distr_prod_cardi = Tex(r'\textbf{(0, N)}', color= BLACK, font_size= 26).next_to(distr_prod.get_start(), DOWN, buff=0.1).shift(RIGHT*0.45)
prod_distr_cardi = Tex(r'\textbf{(1, 1)}', color= BLACK, font_size= 26).next_to(distr_prod.get_end(), UP, buff=0.1).shift(RIGHT*0.45)

cardinality = VGroup(city_distr_cardi, distr_city_cardi, dist_distr_cardi, distr_dist_cardi, distr_prod_cardi, prod_distr_cardi)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(city, dist, prod, distribuition, relation_connectors, cardinality).scale(0.7).shift(DOWN)

#Modelo logico da entidade Cidade:
#------------------------------------------------------------------------------------#
logic_city = Table(
    [["Vancouver"],
    ["London"],
    ["Toronto"],
    ["Amsterdan"],
    ["Melbourne"],
    ["Frankfurt"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name")],
    top_left_entry=Text("Code"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_city.get_entries().set_color(BLACK)
for item in range(2):
    logic_city.add_highlighted_cell((1, item), color= ORANGE)
logic_city.scale(0.35)
#------------------------------------------------------------------------------------#

#Modelo logico da entidade Produto:
#------------------------------------------------------------------------------------#
logic_prod = Table(
    [["CPU"],
    ["Memory"],
    ["Monitor"],
    ["Keyboard"],
    ["Hard Drive"],
    ["Cooler"]],
    row_labels=[Text("101"), Text("102"), Text("103"), Text("104"), Text("105"), Text("106")],
    col_labels=[Text("Name")],
    top_left_entry=Text("Code"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_prod.get_entries().set_color(BLACK)
for item in range(2):
    logic_prod.add_highlighted_cell((1, item), color= ORANGE)
logic_prod.scale(0.35)
#------------------------------------------------------------------------------------#

#Modelo logico da entidade Distribuidora:
#------------------------------------------------------------------------------------#
logic_dist = Table(
    [["MegaMix"],
    ["Hayamax"],
    ["L&R"],
    ["Arrow"],
    ["Mouser"],
    ["Enesco"]],
    row_labels=[Text("111"), Text("112"), Text("113"), Text("114"), Text("115"), Text("116")],
    col_labels=[Text("Name")],
    top_left_entry=Text("Code"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_dist.get_entries().set_color(BLACK)
for item in range(2):
    logic_dist.add_highlighted_cell((1, item), color= ORANGE)
logic_dist.scale(0.35)
#------------------------------------------------------------------------------------#

#Modelo logico da relacao em New Relation:
#------------------------------------------------------------------------------------#
dist_new = Table(
   [["01", "101", "111"],
    ["02", "102", "112"],
    ["03", "103", "113"],
    ["04", "104", "114"],
    ["05", "105", "115"],
    ["06", "106", "116"]],
    row_labels=[Text("08/08/2008"), Text("09/08/2009"), Text("10/02/2009"), Text("05/12/2008"), Text("03/05/2015"), Text("09/01/2015")],
    col_labels=[Text("City_ID"), Text("Prod_ID"), Text("Dist_ID")],
    top_left_entry=Text("Starting_Date"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
for item in range(4):
    dist_new.add_highlighted_cell((1, item+1), color= ORANGE)
    dist_new.get_columns()[item].set_color(BLACK)
dist_new.scale(0.35)
#------------------------------------------------------------------------------------#



class Introduction(Scene):
    def construct(self):
        #Parte 1: Introducao do Grau > 2 e modelo exemplo
        intro = Tex("In all previous cases, we saw an example where one entity had a relationship with one other entity.", color= BLACK, font_size= 32).next_to(relation, UP, buff=2)
        intro_2 = Tex("It is possible, however, for an entity to be related to two or more entities.", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= 0.25)
        intro_3 = Tex("Take this Entity-Relationship Diagram as example:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff= 0.25)

        self.play(Write(intro), run_time= 3)
        self.wait(4)
        self.play(Write(intro_2))
        self.wait(3)
        self.play(Write(intro_3))
        self.wait(2)
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait(3)

        #Parte 2: Indicar Metodo
        to_elim = VGroup(intro, intro_2, intro_3)
        intro = Tex("The proper way to model this type of relationship is by creating a new table for the relationship.", color= BLACK, font_size= 32).next_to(relation, UP, buff=2)
        intro_2 = Tex("This way, all entities will have their own tables:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= MED_SMALL_BUFF)
        self.play(FadeOut(to_elim))
        self.play(Write(intro))
        self.wait(3)
        self.play(Write(intro_2))
        self.wait(3)

        #Parte 3: Criacao das tables das entidades
        to_elim = VGroup(intro, intro_2)
        relation.generate_target()
        relation.target.move_to([0, 1.5, 0]).scale(0.7)

        self.play(FadeOut(to_elim))
        self.play(MoveToTarget(relation))
        self.wait()

        logic_city.move_to([[-3.5, -2, 0]])
        logic_prod.move_to([[0, -2, 0]])
        logic_dist.move_to([[3.5, -2, 0]])
        path = ArcBetweenPoints(start= city.get_center(), end= logic_city.get_center(), angle= 1.7)
        path2 = Line(start= prod.get_center(), end= logic_prod.get_center())
        path3 = ArcBetweenPoints(start= dist.get_center(), end= logic_dist.get_center(), angle= -1.7)
        
        city_copy = city.copy()
        prod_copy = prod.copy()
        dist_copy = dist.copy()

        self.play(MoveAlongPath(city_copy, path))
        self.wait()
        self.play(FadeTransform(city_copy, logic_city))
        self.wait()
        self.play(MoveAlongPath(prod_copy, path2))
        self.wait()
        self.play(FadeTransform(prod_copy, logic_prod))
        self.wait()
        self.play(MoveAlongPath(dist_copy, path3))
        self.wait()
        self.play(FadeTransform(dist_copy, logic_dist))
        self.wait(2)

        #Parte 4: Transformacao da table de relacao
        desc = Tex("The relationship will also have its own table:", color= BLACK, font_size= 32).next_to(relation, UP, buff= MED_SMALL_BUFF)
        dist_new.move_to([0, 1.5, 0])

        left_part = VGroup(city, distr_city, distr_city_cardi, city_distr_cardi)
        bottom_part = VGroup(prod, distr_prod, distr_prod_cardi, prod_distr_cardi)
        right_part = VGroup(dist, distr_dist, distr_dist_cardi, dist_distr_cardi)

        self.play(Write(desc))
        self.wait(2)
        self.play(FadeOut(desc))
        self.wait()
        self.play(FadeOut(left_part, shift= UL),
                  FadeOut(bottom_part, shift= DOWN),
                  FadeOut(right_part, shift= UR))
        self.wait(2)
        self.play(FadeTransform(distribuition, dist_new))
        self.wait(2)

        #Parte 5: Explicar chaves estrangeiras
        desc = Tex("Next, the primary key of each entity will be a foreign key to the relationship's table.", color= BLACK, font_size= 32).next_to(relation, UP, buff= SMALL_BUFF)

        p1 = Point(logic_city.get_columns()[0].get_top()).shift(UP*0.45)
        pi = Point(logic_city.get_columns()[0].get_top()).shift(UP*0.1)
        line = Arrow(p1, pi, max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p2 = p1.copy().shift(UR*0.1)
        arco = ArcBetweenPoints(start= p1.get_center(), end= p2.get_center(), angle = -PI/2).set_color(PURE_RED)
        p3 = Point(dist_new.get_columns()[1].get_bottom()).shift(DOWN*0.43)
        pi = Point(dist_new.get_columns()[1].get_bottom()).shift(DOWN*0.1)
        line2 = Arrow(p3, pi, max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p4 = p3.copy().shift(DL*0.1)
        arco2 = ArcBetweenPoints(start= p3.get_center(), end= p4.get_center(), angle = -PI/2).set_color(PURE_RED)
        line3 = Line(arco.get_end(), arco2.get_end()).set_color(PURE_RED)
        key = Tex("FK", color= PURE_RED, font_size= 30).next_to(line3.get_center(), UP, SMALL_BUFF)

        fk = VGroup(line, arco, line3, arco2, line2, key)

        p1 = Point(logic_prod.get_columns()[0].get_top()).shift(UP*0.35)
        pi = Point(logic_prod.get_columns()[0].get_top()).shift(UP*0.1)
        line = Arrow(p1, pi, max_stroke_width_to_length_ratio= 15, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p2 = p1.copy().shift(UR*0.1)
        arco = ArcBetweenPoints(start= p1.get_center(), end= p2.get_center(), angle = -PI/2).set_color(PURE_RED)
        p3 = Point(dist_new.get_columns()[2].get_bottom()).shift(DOWN*0.48)
        pi = Point(dist_new.get_columns()[2].get_bottom()).shift(DOWN*0.1)
        line2 = Arrow(p3, pi, max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p4 = p3.copy().shift(DL*0.1)
        arco2 = ArcBetweenPoints(start= p3.get_center(), end= p4.get_center(), angle = -PI/2).set_color(PURE_RED)
        line3 = Line(arco.get_end(), arco2.get_end()).set_color(PURE_RED)
        key = Tex("FK", color= PURE_RED, font_size= 30).next_to(line3.get_center(), UP, SMALL_BUFF)

        fk2 = VGroup(line, arco, line3, arco2, line2, key)

        p1 = Point(logic_dist.get_columns()[0].get_top()).shift(UP*0.43)
        pi = Point(logic_dist.get_columns()[0].get_top()).shift(UP*0.1)
        line = Arrow(p1, pi, max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p2 = p1.copy().shift(UL*0.1)
        arco = ArcBetweenPoints(start= p1.get_center(), end= p2.get_center(), angle = PI/2).set_color(PURE_RED)
        p3 = Point(dist_new.get_columns()[3].get_bottom()).shift(DOWN*0.43)
        pi = Point(dist_new.get_columns()[3].get_bottom()).shift(DOWN*0.1)
        line2 = Arrow(p3, pi, max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        p4 = p3.copy().shift(DR*0.1)
        arco2 = ArcBetweenPoints(start= p3.get_center(), end= p4.get_center(), angle = PI/2).set_color(PURE_RED)
        line3 = Line(arco.get_end(), arco2.get_end()).set_color(PURE_RED)
        key = Tex("FK", color= PURE_RED, font_size= 30).next_to(line3.get_center(), UP, SMALL_BUFF)

        fk3 = VGroup(line, arco, line3, arco2, line2, key)

        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(desc))
        self.wait()
        self.play(Create(fk))
        self.wait(3)
        self.play(Create(fk2))
        self.wait(3)
        self.play(Create(fk3))
        self.wait(5)