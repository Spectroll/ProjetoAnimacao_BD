from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

class BothOptional_Method2(Scene):
    def construct(self):
        #Bloco para relacao marriage:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        marriage_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
        marriage_title = Text("Marriage", color = BLACK, font_size=24).move_to(marriage_shape.get_center())
        marriage_att = Circle(radius = 0.1, color= BLACK, fill_opacity= 0).next_to(marriage_shape.get_bottom(), DOWN)
        marriage_att_date = Text("Date", color= BLACK, font_size=15).next_to(marriage_att, DOWN, buff=0.1)
        marriage_att_connect = Line(start= marriage_shape.get_bottom(), end= marriage_att.get_top(), color= BLACK)

        marriage = VGroup(marriage_shape, marriage_title, marriage_att, marriage_att_date, marriage_att_connect)
        #---------------------------------------------------------------------------------------------------------------------------------------#	

        #Bloco para a entidade Pessoa:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        person_title = Text("Person", color = BLACK, font_size= 24)
        person_shape = SurroundingRectangle(person_title, color = BLACK, buff = 0.4)
        person_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(person_shape.get_bottom(), DL*1.5)
        person_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(person_shape.get_bottom(), DOWN)
        person_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(person_att, DOWN, buff= 0.05)
        person_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(person_att2, DOWN, buff= 0.05)
        person_att_con = Line(start= [-0.475, -0.55, 0], end= person_att.get_top(), color= BLACK)
        person_att_con2 = Line(start= person_shape.get_bottom(), end= person_att2.get_top(), color= BLACK)

        person = VGroup(person_title, person_shape, person_att, person_att2, person_att_code, person_att_name, person_att_con, person_att_con2)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        relation = VGroup(person, marriage).arrange(buff= 1)

        #Relacoes entre os blocos:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        person_marriage_con_1 = Line(start= [-1.1, 0.9, 0], end= [-1.1, 1.2, 0], buff= 3, color= BLACK)
        person_marriage_con_2 = Line(start= [-1.1, -0.11, 0], end= [-1.1, -0.4, 0], buff= 3, color= BLACK)
        person_marriage_con_3 = Line(start= person_marriage_con_1.get_end(), end = [1, 1.2, 0], color= BLACK)
        person_marriage_con_4 = Line(start= person_marriage_con_2.get_end(), end = [1, -0.4, 0], color= BLACK)
        person_marriage_con_5 = Line(start= person_marriage_con_3.get_end(), end = [1, 0.98, 0], color= BLACK)
        person_marriage_con_6 = Line(start= person_marriage_con_4.get_end(), end = [1, -0.26, 0], color= BLACK)
        relation_conectors = VGroup(person_marriage_con_1, person_marriage_con_2, person_marriage_con_3, person_marriage_con_4, person_marriage_con_5, person_marriage_con_6)

        person_marriage_cardi_1 = Tex("(0, 1)", color= BLACK, font_size= 24).next_to(person_marriage_con_3, UP, buff=0.05)
        person_marriage_cardi_2 = Tex("(0, 1)", color= BLACK, font_size= 24).next_to(person_marriage_con_4, DOWN, buff=0.1)
        cardinality = VGroup(person_marriage_cardi_1, person_marriage_cardi_2)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        relation = VGroup(relation, relation_conectors, cardinality)
        relation.scale(0.75)


        #---------------------------------------------------------------------------------------------------------------------------------------#
        logic_person = Table(
            [["Veronica", "08-08-2007"],
			["Roger", "NULL"],
			["Elisa", "04-01-2002"],
			["Billy", "NULL"],
			["Adam", "04-01-2002"],
			["Alex", "08-08-2007"]],
			row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
			col_labels=[Text("Name"), Text("Marriage_Date")],
			top_left_entry=Text("ID"),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([0, -2, 0])
        logic_person.get_entries().set_color(BLACK)
        logic_person.get_columns()[2].set_color(WHITE)
        logic_person.add_highlighted_cell((1, 1), color= ORANGE)
        logic_person.add_highlighted_cell((1, 2), color= ORANGE)  
        logic_person.scale(0.4)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        #Parte 1: Apresentacao metodo da adicao de atributos
        title = Tex("Method 2: Attribute adding", color= BLACK, font_size= 36).move_to([-4.7, 3.7, 0])
        desc = Tex("For this method, we simply add the relationship's attributes directly to the entity's table", color= BLACK, font_size= 32).next_to(relation, UP, buff=1)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP*1.5), run_time= 2)
        self.play(Write(desc))
        self.wait(3)

        #Parte 2: Transforma Person conceitual em logico    

        self.play(FadeOut(desc))
        self.play(relation.animate.shift(UP * 2.5))

        path = ArcBetweenPoints(start= person.get_center(), end= [0, -2.5, 0], angle= 0.5)
        person_copy = person.copy()
        
        self.play(MoveAlongPath(person_copy, path= path))
        self.wait()
        self.play(FadeTransform(person_copy, logic_person))
        self.wait(2)

        #Parte 3: Destacar atributos do relacionamento e adicionar ao modelo logico de person
        date = VGroup(marriage_att, marriage_att_connect, marriage_att_date)
        path = ArcBetweenPoints(start= date.get_center(), end= [3.5, -2.35, 0], angle= -1.7)
        column_copy = logic_person.get_columns()[2].copy()
        column_copy.set_color(BLACK)
        date_copy = date.copy()

        self.play(MoveAlongPath(date_copy, path))
        self.play(Circumscribe(date_copy, Circle, fade_out= True, color= PURE_RED))
        self.wait()
        self.play(ReplacementTransform(date_copy, column_copy))
        logic_person.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        #Parte 4: Representar o relacionamento pela chave estrangeira
        exp = Tex("The relationship will be represented as a Foreign Key between two instances of Person:", color= BLACK, font_size= 32).next_to(relation, DOWN)
        logic_person_group = VGroup(logic_person, column_copy)
        logic_person_copy = logic_person_group.copy()
        marriage_copy = marriage.copy()
        marriage_copy.generate_target()
        marriage_copy.target.move_to([0, -0.6, 0])
        marriage_copy.target.scale(0.8)
        line = Line(start= [-4.1, 0, 0], end= [0.75, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [0.85, -0.1, 0], end= [0.85, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        fk = VGroup(line, arco, arco2, line2, line3)
        key = Tex("FK", color= PURE_RED, font_size= 38).next_to(fk, UP, SMALL_BUFF)

        self.play(Write(exp))
        self.wait(2)
        self.play(logic_person_group.animate.shift(LEFT*2.5), FadeIn(logic_person_copy), logic_person_copy.animate.shift(RIGHT*2.5))
        self.wait(2)
        self.play(MoveToTarget(marriage_copy, path_arc= 30 * DEGREES))
        self.wait(2)
        self.play(ReplacementTransform(marriage_copy, fk))
        self.wait()
        self.play(Write(key))
        self.wait()

        #Parte 5:
        final = VGroup(fk, key, logic_person_group, logic_person_copy)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Pro n1", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Pro n2", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Con n1", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        con_2 = Tex("-Con n2", color= BLACK, font_size= 40).next_to(con_1, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2.5, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeOut(exp))
        self.play(final.animate.scale(0.75))
        self.play(final.animate.shift(RIGHT*3), anim, run_time= 3)
        self.wait()
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(con_1))
        self.play(Write(con_2))
        self.wait(2)

class BothOptional_Method3(Scene):
    def construct(self):
        #Bloco para relacao marriage:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        marriage_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
        marriage_title = Text("Marriage", color = BLACK, font_size=24).move_to(marriage_shape.get_center())
        marriage_att = Circle(radius = 0.1, color= BLACK, fill_opacity= 0).next_to(marriage_shape.get_bottom(), DOWN)
        marriage_att_date = Text("Date", color= BLACK, font_size=15).next_to(marriage_att, DOWN, buff=0.1)
        marriage_att_connect = Line(start= marriage_shape.get_bottom(), end= marriage_att.get_top(), color= BLACK)

        marriage = VGroup(marriage_shape, marriage_title, marriage_att, marriage_att_date, marriage_att_connect)
        #---------------------------------------------------------------------------------------------------------------------------------------#	

        #Bloco para a entidade Pessoa:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        person_title = Text("Person", color = BLACK, font_size= 24)
        person_shape = SurroundingRectangle(person_title, color = BLACK, buff = 0.4)
        person_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(person_shape.get_bottom(), DL*1.5)
        person_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(person_shape.get_bottom(), DOWN)
        person_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(person_att, DOWN, buff= 0.05)
        person_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(person_att2, DOWN, buff= 0.05)
        person_att_con = Line(start= [-0.475, -0.55, 0], end= person_att.get_top(), color= BLACK)
        person_att_con2 = Line(start= person_shape.get_bottom(), end= person_att2.get_top(), color= BLACK)

        person = VGroup(person_title, person_shape, person_att, person_att2, person_att_code, person_att_name, person_att_con, person_att_con2)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        relation = VGroup(person, marriage).arrange(buff= 1)

        #Relacoes entre os blocos:
        #---------------------------------------------------------------------------------------------------------------------------------------#
        person_marriage_con_1 = Line(start= [-1.1, 0.9, 0], end= [-1.1, 1.2, 0], buff= 3, color= BLACK)
        person_marriage_con_2 = Line(start= [-1.1, -0.11, 0], end= [-1.1, -0.4, 0], buff= 3, color= BLACK)
        person_marriage_con_3 = Line(start= person_marriage_con_1.get_end(), end = [1, 1.2, 0], color= BLACK)
        person_marriage_con_4 = Line(start= person_marriage_con_2.get_end(), end = [1, -0.4, 0], color= BLACK)
        person_marriage_con_5 = Line(start= person_marriage_con_3.get_end(), end = [1, 0.98, 0], color= BLACK)
        person_marriage_con_6 = Line(start= person_marriage_con_4.get_end(), end = [1, -0.26, 0], color= BLACK)
        relation_conectors = VGroup(person_marriage_con_1, person_marriage_con_2, person_marriage_con_3, person_marriage_con_4, person_marriage_con_5, person_marriage_con_6)

        person_marriage_cardi_1 = Tex("(0, 1)", color= BLACK, font_size= 24).next_to(person_marriage_con_3, UP, buff=0.05)
        person_marriage_cardi_2 = Tex("(0, 1)", color= BLACK, font_size= 24).next_to(person_marriage_con_4, DOWN, buff=0.1)
        cardinality = VGroup(person_marriage_cardi_1, person_marriage_cardi_2)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        relation = VGroup(relation, relation_conectors, cardinality).move_to([0, 1, 0])
        relation.scale(0.75)

        #---------------------------------------------------------------------------------------------------------------------------------------#
        logic_person = Table(
            [["Veronica"],
			["Roger"],
			["Elisa"],
			["Billy"],
			["Adam"],
			["Alex"]],
			row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
			col_labels=[Text("Name")],
			top_left_entry=Text("ID"),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([-2, -2.35, 0])
        logic_person.get_entries().set_color(BLACK)
        logic_person.add_highlighted_cell((1, 1), color= ORANGE)
        logic_person.add_highlighted_cell((1, 2), color= ORANGE)  
        logic_person.scale(0.4)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        #---------------------------------------------------------------------------------------------------------------------------------------#
        logic_marriage = Table(
            [["08-08-2007"],
			["04-01-2002"],
			["04-01-2002"],
			["08-08-2007"]],
            row_labels=[Text("01"), Text("03"), Text("05"), Text("06")],
			col_labels=[Text("Marriage_Date")],
            top_left_entry=Text("ID"),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([2, -2, 0])
        logic_marriage.get_entries().set_color(BLACK)
        logic_marriage.get_columns()[0].set_color(WHITE)
        logic_marriage.add_highlighted_cell((1, 2), color= ORANGE)
        logic_marriage.scale(0.4)
        #---------------------------------------------------------------------------------------------------------------------------------------#

        #Parte 1: apresentacao do metodo de nova relacao
        title = Tex("Method 3: New Relation", color= BLACK, font_size= 36).move_to([-4.7, 3.7, 0])
        desc = Tex("For this method, we'll have the entity's table, as well as a new table for the relationship, containing all of its attributes.", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        path = ArcBetweenPoints(start= person.get_center(), end= [-2, -2.5, 0], angle= 1.7)
        path2 = ArcBetweenPoints(start= marriage.get_center(), end= [2, -2, 0], angle= -1.7)
        person_copy = person.copy()
        marriage_copy = marriage.copy()

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.play(Write(desc))
        self.wait(3)
        self.play(MoveAlongPath(person_copy, path))
        self.wait()
        self.play(FadeTransform(person_copy, logic_person))
        self.wait()
        self.play(MoveAlongPath(marriage_copy, path2))
        self.wait()
        self.play(FadeTransform(marriage_copy, logic_marriage))
        self.wait(3)

        #Parte 2: destacar a chave primaria da entidade
        to_elim = desc
        desc = Tex("Next, we add the entity's primary key as a foreign key to the new table.", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        id = VGroup(person_att, person_att_code, person_att_con)
        box_pk = SurroundingRectangle(id, corner_radius= 0.25, buff= 0.2, color= PURE_RED)
        arr_pk = CurvedArrow(start_point= box_pk.get_left(), end_point= [-3, 1, 0], color= PURE_RED, angle= -PI/4)
        desc_pk = Tex("Primary key", color= PURE_RED, font_size= 32).move_to([-4, 1, 0])

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(desc))
        self.wait()
        self.play(Create(box_pk))
        self.wait()
        self.play(Create(arr_pk))
        self.wait()
        self.play(Write(desc_pk))
        self.wait(2)

        #Parte 3: Adicionar a chave primaria da entidade a nova relacao marriage e identificar chave estrangeira
        to_elim = VGroup(box_pk, arr_pk, desc_pk)
        box_fk = SurroundingRectangle(logic_marriage.get_columns()[0], corner_radius= 0.2, buff= 0.25, color= PURE_RED)
        box_fk2 = SurroundingRectangle(logic_person.get_columns()[0], corner_radius= 0.2, buff= 0.25, color= PURE_RED)
        arr_fk = CurvedArrow(start_point= box_fk.get_top(), end_point= box_fk2.get_top(), color= PURE_RED, angle= PI/4)
        desc_fk = Tex("Foreign key", color= PURE_RED, font_size= 32).next_to(arr_fk, UP, SMALL_BUFF)
        path = ArcBetweenPoints(start= id.get_center(), end= [0, -2, 0])
        column_copy = logic_marriage.get_columns()[0].copy()
        column_copy.set_color(BLACK)
        id_copy = id.copy()

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(MoveAlongPath(id_copy, path))
        self.play(Circumscribe(id_copy, Circle, fade_out= True, color= PURE_RED))
        self.wait()
        self.play(FadeTransform(id_copy, column_copy))
        logic_marriage.add_highlighted_cell((1, 1), color= ORANGE)
        logic_marriage2 = VGroup(logic_marriage, column_copy)
        self.wait()
        self.play(Create(box_fk), Create(box_fk2))
        self.wait()
        self.play(Create(arr_fk))
        self.wait()
        self.play(Write(desc_fk))
        self.wait(2)

        #Parte 4
        to_elim = (desc)
        path = ArcBetweenPoints(start= relation.get_center(), end= [-3, -2.5, 0])
        move = MoveAlongPath(relation, path)
        relation_group = VGroup(logic_marriage2, box_fk, box_fk2, arr_fk, desc_fk, logic_person)
        pros = Tex("PROS:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Pro n1", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Pro n2", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        cons = Tex("CONS:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Con n1", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        con_2 = Tex("-Con n2", color= BLACK, font_size= 40).next_to(con_1, DOWN, buff= 0.25)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(move, relation_group.animate.shift(RIGHT*3), run_time= 3)
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(con_1))
        self.play(Write(con_2))
        self.wait(2)

class test(Scene):
    def construct(self):
        line = Line(start= LEFT, end= RIGHT).set_color(PURE_RED)
        line2= Arrow(start= [1.1, -0.1, 0], end= [1.1, -0.5, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-1.1, -0.1, 0], end= [-1.1, -0.5, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)

        linha = VGroup(line, arco, arco2, line2, line3)
        self.play(FadeIn(linha))
        self.wait()