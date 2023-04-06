from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

class BothOptional(Scene):
	def construct(self):
		#Modelo logico da entidade mulher:
		#------------------------------------------------------------------------------------#
		logic_person = Table(
			[["Veronica"],
			["Roger"],
			["Elisa"],
			["Billy"],
			["Adam"],
			["Alex"]],
			row_labels=[Text("01", color= BLACK), Text("02", color= BLACK), Text("03", color= BLACK), Text("04", color= BLACK), Text("05", color= BLACK), Text("06", color= BLACK)],
			col_labels=[Text("Name", color= BLACK)],
			top_left_entry=Text("ID", color= BLACK),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([-2.5, -2, 0])
		logic_person.get_entries().set_color(BLACK)
		for item in range(2):
			logic_person.add_highlighted_cell((1, item), color= ORANGE)
		logic_person.scale(0.4)
		#------------------------------------------------------------------------------------#

		#Modelo logico da entidade Casamento
		#---------------------------------------------------------------------------------------------------------------------------#
		logic_marriage = Table(
			[["08-08-2007"],
			["NULL"],
			["04-01-2002"],
			["NULL"],
			["04-01-2002"],
			["08-08-2007"]],
			col_labels=[Text("Date", color= BLACK)],
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([2.5, -2, 0])
		logic_marriage.get_entries().set_color(BLACK)
		logic_marriage.add_highlighted_cell((1, 1), color= ORANGE)
		logic_marriage.scale(0.4)
		#---------------------------------------------------------------------------------------------------------------------------#

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

		#Parte 1: Introducao de 1:1 e modelo exemplo
		intro = Tex("We create one-to-one optional relationships when two entities may or may not have a relationship between them.", color= BLACK, font_size= 32).next_to(relation, UP, buff=1.5)
		intro_2 = Tex("Take this Entity-Relationship Diagram as example:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff=0.5)
		self.play(Write(intro))
		self.wait(5)
		self.play(Write(intro_2))
		self.wait()
		self.play(FadeIn(relation, shift= UP), run_time= 2)
		self.wait(2)

		#Parte 2: Explicacao e indicacao da cardinalidade 1:1
		to_elim = VGroup(intro_2)
		intro_2 = Tex("One-to-One optional relationships are identified with cardinality 0 to 1 like this:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff=0.5)

		self.play(FadeOut(to_elim))
		self.wait()
		self.play(Write(intro_2))
		self.wait(2)
		self.play(relation.animate.shift(DOWN * 1.5))
		self.play(relation.animate.scale(1.5))
		for _ in range(2):
			self.play(Indicate(cardinality, color= PURE_RED)) 
		self.play(relation.animate.scale(0.5))
		self.wait(2)

		#Parte 3: Apresentacao dos metodos e inicio da fusao de entidade
		to_elim = VGroup(intro, intro_2)
		intro = Tex("There are 3 ways to deal with One-To-One relationships:", color= BLACK, font_size= 32).next_to(relation, UP, buff=3.5)
		intro_2 = Tex("Method 1: Entity Fusion", color= BLACK, font_size= 36).next_to(intro, DOWN, buff= 0.5)
		intro_3 = Tex("Method 2: Attribute adding", color= BLACK, font_size= 36).next_to(intro_2, DOWN, buff= 0.5)
		intro_4 = Tex("Method 3: New relation", color= BLACK, font_size= 36).next_to(intro_3, DOWN, buff= 0.5)
		intro_final = Tex("Let's see how each one of those works!", color= BLACK, font_size= 32).next_to(relation, UP, buff=3.5)

		self.play(FadeOut(to_elim))
		self.play(Write(intro))
		self.wait(2)
		self.play(Write(intro_2))
		self.play(Write(intro_3))
		self.play(Write(intro_4))
		self.wait(2)
		self.play(FadeOut(intro))
		self.play(Write(intro_final))
		self.wait(2)
		self.play(FadeOut(intro, intro_3, intro_4))
		self.wait(2)
		self.play(intro_2.animate.shift(LEFT * 5))
		self.play(intro_2.animate.shift(UP * 1.25))
		self.play(relation.animate.shift(UP * 2.25))
		self.wait()

		#INICIO METODO 1
		#Modelo logico da entidade Casamento e Pessoa mesclados
		#---------------------------------------------------------------------------------------------------------------------------#
		marriage_person_merge = Table(
			[["Veronica","Alex","08-08-2007"],
			["Roger","NULL","NULL"],
			["Elisa","Adam","04-01-2002"],
			["Billy","NULL","NULL"],
			["Adam","Elisa","04-01-2002"],
			["Alex","Veronica","08-08-2007"]],
			row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
			col_labels=[Text("Name"), Text("Married_To"), Text("Date")],
			top_left_entry=Text("ID"),
			include_outer_lines=True,
			line_config= {"color": BLACK},
			v_buff=0.5, h_buff=0.6).move_to([0, -2, 0])
		marriage_person_merge.get_entries().set_color(BLACK)
		for item in range(4):
			marriage_person_merge.add_highlighted_cell((1, item), color= ORANGE)
		marriage_person_merge.scale(0.4)
		#---------------------------------------------------------------------------------------------------------------------------#

		#Parte 1: Introducao do metodo
		intro = Tex("For this method, we are going to merge both entities and the relationship into a single table:", color= BLACK, font_size= 32).next_to(intro_4, UP, buff=1.5)
		self.play(Write(intro))
		person_copy = person.copy()
		person_copy2 = person.copy()
		marriage_copy = marriage.copy()
		self.wait(2)

		#Parte 2: Traz as entidades no modelo conceitual e transforma em logico
		arc = ArcBetweenPoints(start= person.get_center(), end= [-4, -2.5, 0])
		arc2 = ArcBetweenPoints(start= person.get_center(), end= [0, -2.5, 0])
		arc3 = ArcBetweenPoints(start= marriage.get_center(), end= [4, -2.5, 0], angle= -PI/4)

		self.play(MoveAlongPath(person_copy, arc))
		self.wait()
		self.play(MoveAlongPath(person_copy2, arc2))
		self.wait()
		self.play(MoveAlongPath(marriage_copy, arc3))
		self.wait(2)
		logic_person.move_to([-4, -2.5, 0])
		logic_person2 = logic_person.copy()
		logic_person2.move_to([0, -2.5, 0])
		logic_marriage.move_to([4, -2.5, 0])
		self.play(FadeTransform(person_copy, logic_person))
		self.wait(2)
		self.play(FadeTransform(person_copy2, logic_person2))
		self.wait(2)
		self.play(FadeTransform(marriage_copy, logic_marriage))
		self.wait(2)

		#Parte 3: Funde as entidades e relacionamento
		to_merge = VGroup(logic_person, logic_person2, logic_marriage)
		arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2.5, 0])
		anim = MoveAlongPath(relation, arc)

		self.play(FadeTransform(to_merge, marriage_person_merge))
		self.wait(2)
		self.play(marriage_person_merge.animate.shift(RIGHT*3), anim, run_time= 2)
		self.wait()

		#Parte 4: Conclusao
		pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
		pro_1 = Tex("-Eliminates the need for joints", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
		cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
		con_1 = Tex("-Hinders future expansions", color= BLACK, font_size= 32).next_to(cons, DOWN, buff= 0.25)
		con_2 = Tex(r"-Optional attributes may only apply to some records,\\resulting in lots of NULL values", color= BLACK, font_size= 32).next_to(con_1, DOWN, buff= 0.25)

		self.play(FadeOut(intro))
		self.play(Write(pros))
		self.play(Write(cons))
		self.play(Write(pro_1))
		self.play(Write(con_1))
		self.play(Write(con_2))
		self.wait(2)