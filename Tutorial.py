from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 1000

class Tutorial(Scene):
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
        person_att_code = Tex("ID", color= BLACK, font_size= 20).next_to(person_att, DOWN, buff= 0.05)
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

        #Começo da animação

        intro = Tex("Here, we'll present some essential guidance on how to navigate the website and its animations.", color= BLACK, font_size= 36)
        intro.move_to([0, 3, 0])
        intro_foward = Tex("Use the button below to start playing the next scene.", color= BLACK, font_size= 36).next_to(intro, DOWN, buff= 2)
        intro_previous = Tex('You can also return to the previous scene by using the <previous> button', color= BLACK, font_size= 36).next_to(intro, DOWN, buff= 2)
        intro_replay = Tex('Or replay this same section by using the <repeat> button', color= BLACK, font_size= 36).next_to(intro_foward, DOWN)
        arrow = Arrow(start= [3, -3, 0], end= [3, -4, 0], color= PURE_RED, buff=2)

        #Seção de explicação do uso dos botões para controlar a animação

        #Parte 1
        self.play(Write(intro), run_time= 4)
        self.wait(3)
        self.play(Write(intro_foward), run_time= 2)
        self.wait(0.5)
        self.play(FadeIn(arrow, shift= DOWN))
        self.wait()

        #Parte 2
        self.play(FadeOut(intro_foward))
        self.play(Write(intro_previous), run_time= 2)
        self.wait(0.5)
        self.play(arrow.animate.shift(LEFT * 6))
        self.wait()
        self.play(Write(intro_replay), run_time= 2)
        self.wait(0.5)
        self.play(arrow.animate.shift(RIGHT * 3))
        self.wait()

        #Parte 3
        to_elim = VGroup(intro, intro_previous, intro_replay, arrow)
        intro = Tex("The focus of this website is Logical Database Design!", color= BLACK, font_size= 36).move_to([0, 3, 0])
        intro_1 = Tex("So, all of its animations discuss options for TRANSFORMING a conceptual database design into a relational model.", color= BLACK, font_size= 36)
        intro_1.next_to(intro, DOWN)
        intro_concep = Tex("We will use EER diagrams like the one below for each animation.", color= BLACK, font_size= 36).next_to(intro_1, DOWN)
        self.play(ShrinkToCenter(to_elim))
        self.wait()
        self.play(Write(intro), run_time= 2)
        self.wait()
        self.play(Write(intro_1), run_time= 4)
        self.wait(3)
        self.play(Write(intro_concep), run_time= 2)
        self.wait(1.5)
        relation.next_to(intro_concep, DOWN, buff= 1.5)
        self.play(FadeIn(relation, shift= UP))
        self.wait()

        #Parte 4
        to_elim = VGroup(intro, intro_1, intro_concep)
        self.play(FadeOut(to_elim))
        self.play(relation.animate.shift(UP*4))
        arrow_square = CurvedArrow(start_point= [-2.5, 2.6, 0], end_point= [-4, 0, 0], color= BLACK, angle= 3.14/2)
        exp_square = Tex('Squares represent entities', color= BLACK, font_size= 32).move_to([-4, -0.25, 0])
        arrow_diamond = CurvedArrow(start_point= [2.5, 2.55, 0], end_point= [4, 0, 0], color= BLACK, angle= -3.14/2)
        exp_diamond = Tex('Diamond shapes represent relations', color= BLACK, font_size= 32).move_to([4, -0.25, 0])
        arrow_card = Arrow(start= [0, 1.5, 0], end= [0, -1.5, 0], color= BLACK)
        exp_card = Tex('Lines connecting shapes represent how entities relate to one another', color= BLACK, font_size= 32).move_to([0, -1.5, 0])

        self.play(Succession( 
            Create(arrow_square),
            Write(exp_square)
        ))
        self.wait(2)
        self.play(Create(arrow_diamond))
        self.play(Write(exp_diamond))
        self.wait(2)
        self.play(Create(arrow_card))
        self.play(Write(exp_card))
        self.wait(2)

        #Parte 5
        #Modelo logico do segundo bloco da Relação casamento
		#---------------------------------------------------------------------------------------------------------------------------#
        logic_person = Table(
            [["Veronica"],
			["Roger"],
			["Elisa"],
			["Billy"],
			["Adam"],
			["Alex"]],
			row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
			col_labels=[Text("Name", color= ORANGE)],
			top_left_entry=Text("ID", color= ORANGE),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6)
        logic_person.get_entries().set_color(WHITE)
        logic_person.scale(0.5)
        # for item in range(2):
        #     logic_person.add_highlighted_cell((1, item), color= ORANGE)
        #---------------------------------------------------------------------------------------------------------------------------#

        to_elim = VGroup(arrow_card, arrow_diamond, arrow_square, exp_card, exp_diamond, exp_square)
        self.play(FadeOut(to_elim))
        self.play(relation.animate.shift(DOWN*3))
        self.wait()
        to_elim = VGroup(marriage, relation_conectors, cardinality)
        self.play(FadeOut(to_elim, shift= RIGHT))
        self.play(person.animate.shift(RIGHT*1.7))
        self.wait()
        intro = Tex('For relational models, entities are always transformed into RELATIONS.', color= BLACK, font_size= 32).next_to(person, UP, buff= 3)
        intro_1 = Tex('Please take a look at how we are going to show this transformation.', color= BLACK, font_size= 32).next_to(intro, DOWN)
        self.play(Write(intro))
        self.wait()
        self.play(Write(intro_1))
        self.wait(2)
        self.play(person.animate.shift(LEFT*2.5))
        self.wait()
        logic_person.next_to(person, RIGHT * 10)
        self.play(GrowFromEdge(logic_person, UL))
        self.wait()

        #Parte 6
        to_elim = VGroup(intro, intro_1)
        id = VGroup(person_att, person_att_code, person_att_con)
        pk_arr = CurvedArrow(start_point= logic_person.get_entries([1, 1]).get_top(), end_point= [0, 2, 0], color= BLACK)
        pk_arr_0 = CurvedArrow(start_point= person_att_code.get_left(), end_point= [-3, -3, 0], color= BLACK)
        intro = Tex('First attribute will be the PRIMARY KEY', color= BLACK, font_size= 28).move_to([-3, 2, 0])
        intro_0 = Tex('Primary keys are identified by the filled circle', color= BLACK, font_size= 28).next_to(pk_arr_0.get_end(), DOWN*1.5)

        self.play(FadeOut(to_elim))
        self.play(Create(pk_arr))
        self.play(Write(intro))
        self.wait(2)
        self.play(Create(pk_arr_0))
        self.play(Write(intro_0))
        self.wait()
        for _ in range(3):
            self.play(Circumscribe(person_att, color= PURE_RED, shape= Circle, fade_out= True))
        self.wait()

        #Parte 7
        to_elim = VGroup(pk_arr, pk_arr_0, intro, intro_0)
        self.play(FadeOut(to_elim))
        id_copy = id.copy()
        column1_copy = logic_person.get_columns()[0].copy()
        column1_copy.set_color(BLACK)
        path = ArcBetweenPoints(start= id.get_center(), end= [0, 0, 0], angle= 1.7)
        self.play(MoveAlongPath(id_copy, path))
        self.play(Circumscribe(id_copy, Circle, fade_out= True, color= PURE_RED))
        self.wait()
        self.play(ReplacementTransform(id_copy, column1_copy))
        logic_person.add_highlighted_cell((1, 1), color= ORANGE)
        self.wait()

        #Parte 8
        name = VGroup(person_att2, person_att_name, person_att_con2)
        k_arr = CurvedArrow(start_point= logic_person.get_entries([1, 2]).get_top(), end_point= [1.5, 2, 0], color= BLACK)
        k_arr_0 = CurvedArrow(start_point= person_att2.get_right(), end_point= [-2, -3, 0], color= BLACK, angle= -1.57)
        intro = Tex('The following columns will contain all remaining attributes', color= BLACK, font_size= 28).move_to([-2.3, 2, 0])
        intro_0 = Tex('Empty circles represent attributes', color= BLACK, font_size= 28).next_to(k_arr_0.get_end(), DOWN*1.5)

        self.play(Create(k_arr))
        self.play(Write(intro))
        self.wait(2)
        self.play(Create(k_arr_0))
        self.play(Write(intro_0))
        self.wait()
        for _ in range(3):
            self.play(Circumscribe(person_att2, color= PURE_RED, shape= Circle, fade_out= True))
        self.wait()

        #Parte 9
        to_elim = VGroup(k_arr, k_arr_0, intro, intro_0)
        name_copy = name.copy()
        column_copy = logic_person.get_columns()[1].copy()
        column_copy.set_color(BLACK)
        path = ArcBetweenPoints(start= name.get_center(), end= [0, 0, 0], angle= 1.7)

        self.play(FadeOut(to_elim))
        self.play(MoveAlongPath(name_copy, path))
        self.play(Circumscribe(name_copy, Circle, fade_out= True, color= PURE_RED))
        self.wait()
        self.play(ReplacementTransform(name_copy, column_copy))
        logic_person.add_highlighted_cell((1, 2), color= ORANGE)
        self.wait()

        #Parte 10
        to_elim = VGroup(column1_copy, column_copy, logic_person)
        intro = Tex('This type of transformation will be shown as a fade to simplify explanations further. Take a look!', color= BLACK, font_size= 32).next_to([0, 0, 0], UP*10)
        person_copy = person.copy()
        logic_person.get_entries().set_color(BLACK)

        self.play(Write(intro))
        self.wait()
        self.play(FadeOut(column1_copy, column_copy))
        self.play(FadeOut(to_elim, shift= RIGHT))
        self.wait()
        self.play(person_copy.animate.shift(RIGHT * 5))
        self.wait()
        self.play(FadeTransform(person_copy, logic_person))
        self.wait()

        #Parte 11
        to_elim = VGroup(logic_person, person, intro)
        intro = Tex('You may use the sections above to navigate through other types of transformations', color= BLACK, font_size= 38)

        self.play(ShrinkToCenter(to_elim))
        self.play(Write(intro))
        self.wait()
