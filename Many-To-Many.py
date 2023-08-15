from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

# DEPT -> ENG | EMP -> PROJ | WORK -> OP

#Bloco para o relacionamento Atua:
#---------------------------------------------------------------------------------------------------------------------------------------#
op_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
op_title = Text("Operates", color = BLACK, font_size=24).move_to(op_shape.get_center())
op_att = Circle(radius = 0.1, color= BLACK, fill_opacity= 0).next_to(op_shape.get_bottom(), DOWN)
op_att_date = Text("Role", color= BLACK, font_size=16).next_to(op_att, DOWN, buff=0.1)
op_att_connect = Line(start= op_shape.get_bottom(), end= op_att.get_top(), color= BLACK)

op = VGroup(op_shape, op_title, op_att, op_att_date, op_att_connect)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Engenheiro:
#---------------------------------------------------------------------------------------------------------------------------------------#
eng_title = Text("Engineer", color = BLACK, font_size= 24)
eng_shape = SurroundingRectangle(eng_title, color = BLACK, buff = 0.4)
eng_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(eng_shape.get_bottom(), DL*1.5)
eng_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(eng_shape.get_bottom(), DOWN)
eng_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(eng_att, DOWN, buff= 0.05)
eng_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(eng_att2, DOWN, buff= 0.05)
eng_att_con = Line(start= [-0.475, -0.55, 0], end= eng_att.get_top(), color= BLACK)
eng_att_con2 = Line(start= eng_shape.get_bottom(), end= eng_att2.get_top(), color= BLACK)

eng = VGroup(eng_title, eng_shape, eng_att, eng_att_code, eng_att_con, eng_att2, eng_att_name, eng_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Projeto:
#---------------------------------------------------------------------------------------------------------------------------------------#
proj_title = Text("Project", color = BLACK, font_size= 24)
proj_shape = SurroundingRectangle(proj_title, color = BLACK, buff = 0.4)
proj_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(proj_shape.get_bottom(), DL*1.5)
proj_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(proj_shape.get_bottom(), DOWN)
proj_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(proj_att, DOWN, buff= 0.05)
proj_att_name = Tex("Title", color= BLACK, font_size= 20).next_to(proj_att2, DOWN, buff= 0.05)
proj_att_con = Line(start= [-0.475, -0.55, 0], end= proj_att.get_top(), color= BLACK)
proj_att_con2 = Line(start= proj_shape.get_bottom(), end= proj_att2.get_top(), color= BLACK)

proj = VGroup(proj_title, proj_shape, proj_att, proj_att_code, proj_att_con, proj_att2, proj_att_name, proj_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(eng, op, proj).arrange(buff= 1)
eng.shift(DOWN*0.035)
proj.shift(DOWN*0.035)

#Relacoes entre os blocos:
#---------------------------------------------------------------------------------------------------------------------------------------#
eng_op_con = Line(start= eng_shape.get_right(), end= op_shape.get_left(), color= BLACK)
proj_op_con = Line(start= proj_shape.get_left(), end= op_shape.get_right(), color= BLACK)

relation_conectors = VGroup(eng_op_con, proj_op_con)

proj_op_cardi = Tex("(0, N)", color= BLACK, font_size= 24).next_to(proj_op_con, UP, buff=0.05)
eng_op_cardi = Tex("(0, N)", color= BLACK, font_size= 24).next_to(eng_op_con, UP, buff=0.1)

cardinality = VGroup(proj_op_cardi, eng_op_cardi)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(relation, relation_conectors, cardinality).shift(DOWN).scale(0.6)


#Modelo logico da entidade Projeto:
#------------------------------------------------------------------------------------#
logic_proj = Table(
    [["CAD/CAM"],
    ["Maintenance"],
    ["DB Develop"],
    ["Automaton"],
    ["Race Car"],
    ["SD_Drone"]],
    row_labels=[Text("101"), Text("102"), Text("103"), Text("104"), Text("105"), Text("106")],
    col_labels=[Text("Title")],
    top_left_entry=Text("Code"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_proj.get_entries().set_color(BLACK)
for item in range(2):
    logic_proj.add_highlighted_cell((1, item), color= ORANGE)
logic_proj.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da entidade Engenheiro:
#------------------------------------------------------------------------------------#
logic_eng = Table(
    [["Veronica"],
    ["Roger"],
    ["Elisa"],
    ["Billy"],
    ["Adam"],
    ["Alex"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name")],
    top_left_entry=Text("Code"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_eng.get_entries().set_color(BLACK)
for item in range(2):
    logic_eng.add_highlighted_cell((1, item), color= ORANGE)
logic_eng.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da relacao em New Relation:
#------------------------------------------------------------------------------------#
op_new = Table(
   [["01", "101"],
    ["02", "102"],
    ["03", "103"],
    ["04", "104"],
    ["05", "105"],
    ["06", "106"]],
    row_labels=[Text("Draftsman"), Text("Manager"), Text("DevOps"), Text("Developer"), Text("Mechanical"), Text("Technician")],
    col_labels=[Text("Eng_ID"), Text("Project_ID")],
    top_left_entry=Text("Role"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
op_new.add_highlighted_cell((1, 1), color= ORANGE)
op_new.get_columns()[0].set_color(BLACK)
op_new.scale(0.4)
#------------------------------------------------------------------------------------#


class Introduction(Scene):
    def construct(self):
        #Parte 1: Introducao de 0:N e modelo exemplo
        intro = Tex("We create many-to-many relationships when many instances of an entity have a relationship with many instances from another entity.", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_2 = Tex("Take this Entity-Relationship Diagram as example:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= 0.25)

        self.play(Write(intro), run_time= 3)
        self.wait(4)
        self.play(Write(intro_2))
        self.wait(2)
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait(3)

        #Parte 2: Indicar cardinalidade (0:N)
        to_elim = VGroup(intro_2)
        intro_2 = Tex("Optional many-to-many relationships are identified with cardinality 0 to N like this:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff=0.5)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(intro_2))
        self.wait(2)
        self.play(relation.animate.shift(DOWN*0.5).scale(1.75))
        for _ in range(3):  
            self.play(Indicate(cardinality, color= PURE_RED))
        self.wait(2)

        #Parte 3: Apresentacao dos metodos e inicio da Relacao Propria
        to_elim = VGroup(intro, intro_2)
        intro = Tex("The proper way to model this type of relationship is by creating a new table for the relationship.", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_2 = Tex("This way, both entities will have their own tables:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= MED_SMALL_BUFF)
        self.play(FadeOut(to_elim))
        self.play(Write(intro))
        self.wait(3)
        self.play(Write(intro_2))
        self.wait(3)

        #Parte 4: Criacao das tables das entidades
        relation.generate_target()
        relation.target.next_to(intro_2, DOWN, buff= 0.15)
        relation.target.scale(0.6)
        self.play(MoveToTarget(relation))
        self.wait()

        logic_eng.move_to([[-4.5, -2, 0]])
        logic_proj.move_to([[4.5, -2, 0]])
        path = ArcBetweenPoints(start= eng.get_center(), end= logic_eng.get_center(), angle= 1.7)
        path2 = ArcBetweenPoints(start= proj.get_center(), end= logic_proj.get_center(), angle= -1.7)
        
        eng_copy = eng.copy()
        proj_copy = proj.copy()

        self.play(MoveAlongPath(eng_copy, path))
        self.wait()
        self.play(FadeTransform(eng_copy, logic_eng))
        self.wait()
        self.play(MoveAlongPath(proj_copy, path2))
        self.wait()
        self.play(FadeTransform(proj_copy, logic_proj))
        self.wait(2)

        #Parte 5: Transformacao da table de relacao
        to_elim = VGroup(intro_2)
        desc = Tex("The relationship will also have its own table:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= MED_SMALL_BUFF)
        op_new.move_to([0, -2, 0]).scale(0.97)
        path = Line(op.get_center(), op_new.get_center())
        op_copy = op.copy()

        self.play(FadeOut(to_elim))
        self.wait(2)
        self.play(Write(desc))
        self.wait(2)
        self.play(MoveAlongPath(op_copy, path))
        self.wait(2)
        self.play(FadeTransform(op_copy, op_new))
        self.wait()

        #Parte 3: Destaca as chaves primárias
        to_elim = VGroup(desc)
        desc = Tex("The relationship's table will be comprised by the primary keys of the involved entities:", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= MED_SMALL_BUFF)      

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(desc, intro))
        self.wait()
        self.play(relation.animate.shift(UP*1.5))
        self.wait()

        eng_id = VGroup(eng_att, eng_att_con, eng_att_code)
        path_end = Point(op_new.get_columns()[1].get_top()).shift(UP*0.5)
        path_eng_id = ArcBetweenPoints(start= eng_id.get_center(), end= path_end.get_center(), angle= PI/4)
        column_eng_id_copy = op_new.get_columns()[1].copy()
        column_eng_id_copy.set_color(BLACK)
        eng_id_copy = eng_id.copy()

        proj_id = VGroup(proj_att, proj_att_code, proj_att_con)
        path_end_proj = Point(op_new.get_columns()[2].get_top()).shift(UP*0.5)
        path_address = ArcBetweenPoints(start= proj_id.get_center(), end= path_end_proj.get_center(), angle= -PI/4)
        column_proj_id_copy = op_new.get_columns()[2].copy()
        column_proj_id_copy.set_color(BLACK)
        proj_id_copy = proj_id.copy()  

        self.play(Circumscribe(eng_id, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(eng_id_copy, path_eng_id))
        self.wait()
        self.play(ReplacementTransform(eng_id_copy, column_eng_id_copy))
        op_new.add_highlighted_cell((1, 2), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(proj_id, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(proj_id_copy, path_address))
        self.wait()
        self.play(ReplacementTransform(proj_id_copy, column_proj_id_copy))
        op_new.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        #Parte 4: Destaca as chaves estrangeiras
        desc = Tex("Next, the primary key of each entity will be a foreign key to the relationship's table.", color= BLACK, font_size= 30).next_to(relation, DOWN, buff=0.5)
        table_group = VGroup(logic_proj, op_new)
        table_group2 = VGroup(logic_eng, op_new)

        line = Line(start= [-4.9, 0, 0], end= [-0.1, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [0, -0.1, 0], end= [0, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-5, -0.1, 0], end= [-5, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        
        line4 = Line(start= [-3.5, 0, 0], end= [-1.5, 0, 0]).set_color(PURE_RED)
        line5= Arrow(start= [-1.4, -0.1, 0], end= [-1.4, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line6= Arrow(start= [-3.6, -0.1, 0], end= [-3.6, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco3 = ArcBetweenPoints(start= line4.get_end(), end= line5.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco4 = ArcBetweenPoints(start= line4.get_start(), end= line6.get_start()).set_color(PURE_RED)

        fk = VGroup(line, arco, arco2, line2, line3)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT*4.4)

        fk2 = VGroup(line4, arco3, arco4, line5, line6)
        fk2.move_to(table_group2.get_top()).shift(UP*0.25).shift(RIGHT*4.3)
        key = Tex("FK", color= PURE_RED, font_size= 38).next_to(fk, UP, SMALL_BUFF)
        key2 = key.copy().next_to(fk2, UP, SMALL_BUFF)

        self.play(Write(desc))
        self.wait(3)
        self.play(Create(fk))
        self.wait()
        self.play(Create(fk2))
        self.wait()
        self.play(Write(key))
        self.wait()
        self.play(Write(key2))
        self.wait(3)
        self.play(FadeOut(desc))
        self.wait(5)