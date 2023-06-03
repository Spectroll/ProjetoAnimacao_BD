from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

#Bloco para relacao Possui:
#---------------------------------------------------------------------------------------------------------------------------------------#
has_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
has_title = Text("Has", color = BLACK, font_size=24).move_to(has_shape.get_center())

manage = VGroup(has_shape, has_title)
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

person = VGroup(person_title, person_shape, person_att, person_att_code, person_att_con, person_att2, person_att_name, person_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Passaporte:
#---------------------------------------------------------------------------------------------------------------------------------------#
passp_title = Text("Passport", color = BLACK, font_size= 24)
passp_shape = SurroundingRectangle(passp_title, color = BLACK, buff = 0.4)
passp_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(passp_shape.get_bottom(), DL*1.5)
passp_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(passp_att, DOWN, buff= 0.05)
passp_att_con = Line(start= [-0.475, -0.55, 0], end= passp_att.get_top(), color= BLACK)

passp = VGroup(passp_title, passp_shape, passp_att, passp_att_code, passp_att_con)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(person, manage, passp).arrange(buff= 1)
passp.shift(DOWN*0.38)
person.shift(DOWN*0.38)

#Relacoes entre os blocos:
#---------------------------------------------------------------------------------------------------------------------------------------#
person_manage_con = Line(start= person_shape.get_right(), end= manage.get_left(), color= BLACK)
passp_manage_con = Line(start= passp_shape.get_left(), end= manage.get_right(), color= BLACK)

relation_conectors = VGroup(person_manage_con, passp_manage_con)

passp_manage_cardi = Tex("(0, 1)", color= BLACK, font_size= 24).next_to(passp_manage_con, UP, buff=0.05)
person_manage_cardi = Tex("(1, 1)", color= BLACK, font_size= 24).next_to(person_manage_con, UP, buff=0.1)

cardinality = VGroup(passp_manage_cardi, person_manage_cardi)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(relation, relation_conectors, cardinality).shift(DOWN).scale(0.6)

#Modelo logico da entidade Pessoa:
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

#Modelo logico da entidade Passaporte:
#------------------------------------------------------------------------------------#
logic_passp = Table(
    [["02"],
    ["03"],
    ["05"],
    ["06"]],
    col_labels=[Text("ID", color= BLACK)],
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([-2.5, -2, 0])
logic_passp.get_entries().set_color(BLACK)
logic_passp.add_highlighted_cell((1, 1), color= ORANGE)
logic_passp.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da relacao Possui:
#---------------------------------------------------------------------------------------------------------------------------#
logic_manage = Table(
    [["NULL"],
    ["02"],
    ["03"],
    ["NULL"],
    ["05"],
    ["06"]],
    row_labels=[Text("01", color= BLACK), Text("02", color= BLACK), Text("03", color= BLACK), Text("04", color= BLACK), Text("05", color= BLACK), Text("06", color= BLACK)],
    col_labels=[Text("Passport_ID", color= BLACK)],
    top_left_entry=Text("Person_ID", color= BLACK),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -2.45, 0])
logic_manage.get_entries().set_color(BLACK)
for item in range(2):
    logic_manage.add_highlighted_cell((1, item), color= ORANGE)
logic_manage.scale(0.4)
#---------------------------------------------------------------------------------------------------------------------------#

#Modelo logico de posse no metodo Fusao de Entidades
#---------------------------------------------------------------------------------------------------------------------------#
manage_merge = Table(
    [["Veronica","NULL"],
    ["Roger","02"],
    ["Elisa","03",],
    ["Billy","NULL"],
    ["Adam","05"],
    ["Alex","06"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name"), Text("Passport_ID")],
    top_left_entry=Text("ID"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -2, 0])
manage_merge.get_entries().set_color(BLACK)
for item in range(3):
    manage_merge.add_highlighted_cell((1, item), color= ORANGE)
manage_merge.scale(0.4)
#---------------------------------------------------------------------------------------------------------------------------#

#Modelo logico de empregado no metodo Adicao de Atributos
#---------------------------------------------------------------------------------------------------------------------------#
person_att_adding = Table(
    [["Veronica","14","Marketing"],
    ["Roger","NULL","NULL"],
    ["Elisa","11","Finance",],
    ["Billy","13","Comercial"],
    ["Adam","NULL","NULL"],
    ["Alex","12","Administrative"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name"), Text("Manages_Dept_Code"), Text("Manages_Dept_Name")],
    top_left_entry=Text("ID"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -2, 0])
for i in range(2):
    person_att_adding.add_highlighted_cell((1, i+1), color= ORANGE)
    person_att_adding.get_columns()[i].set_color(BLACK)
person_att_adding.scale(0.4)
#---------------------------------------------------------------------------------------------------------------------------#

# Setas para indicacao da chave estrangeira
#---------------------------------------------------------------------------------------------------------------------------#
line = Line(start= [-4.1, 0, 0], end= [0.75, 0, 0]).set_color(PURE_RED)
line2= Arrow(start= [0.85, -0.1, 0], end= [0.85, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
line3= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
fk = VGroup(line, arco, arco2, line2, line3)
#---------------------------------------------------------------------------------------------------------------------------#


#Arquivo da animacao de introducao
class Introduction(Scene):
    def construct(self):
        #Parte 1: Introducao de 1:1 (um lado opcional) e modelo exemplo
        intro = Tex("We create one-to-one optional relationships when two entities may or may not have a relationship between them.", color= BLACK, font_size= 32).next_to(relation, UP, buff=3.5)
        intro_2 = Tex("In the following case, only one side of the relation will be optional, while the other is mandatory", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= 0.25)        
        intro_3 = Tex("Take this Entity-Relationship Diagram as example:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff= 0.25)
        self.play(Write(intro), run_time= 3)
        self.wait(4)
        self.play(Write(intro_2), run_time= 3)
        self.wait(4)
        self.play(Write(intro_3))
        self.wait(2)
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait(3)

        #Parte 2: Indicar cardinalidade (0:1) e (1:1)
        to_elim = VGroup(intro_3)
        intro_3 = Tex("OPTIONAL One-to-One relationships are identified with cardinality 0 to 1 like this:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff=0.5)
        intro_4 = Tex("MANDATORY One-to-One relationships are identified with cardinality 1 to 1 like this:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff=0.5)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(intro_3))
        self.wait(2)
        self.play(relation.animate.scale(1.5))
        for _ in range(2):  
            self.play(Indicate(passp_manage_cardi, color= PURE_RED))
        self.wait()
        self.play(FadeOut(intro_3))
        self.wait()
        self.play(Write(intro_4))
        self.wait(2)
        for _ in range(2):  
            self.play(Indicate(person_manage_cardi, color= PURE_RED))
        self.wait()
        self.play(relation.animate.scale(0.75))
        self.wait(2)

        #Parte 3: Apresentacao dos metodos e inicio da fusao de entidade
        to_elim = VGroup(intro, intro_2, intro_4)
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
        self.wait(5)

class Entity_Fusion(Scene):
    def construct(self):
        #Parte 1: Introducao do metodo
        relation.move_to([0, 0.75, 0])
        title = Tex("Method 1: Entity Fusion", color= BLACK, font_size= 36).move_to([-5, 3.75, 0])
        intro = Tex("For this method, we are going to merge both entities and the relationship into a single table:", color= BLACK, font_size= 32).next_to(relation, UP, buff= 1)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait()
        self.play(Write(intro))
        self.wait(2)
        person_copy = person.copy()
        passp_copy = passp.copy()
        
        #Parte 2: Traz as entidades no modelo conceitual e transforma em logico
        arc = ArcBetweenPoints(start= person.get_center(), end= [-2.5, -2.5, 0])
        arc2 = ArcBetweenPoints(start= passp.get_center(), end= [2.5, -2.5, 0], angle= -PI/4)

        self.play(MoveAlongPath(person_copy, arc))
        self.wait()
        self.play(MoveAlongPath(passp_copy, arc2))
        self.wait(2)
        logic_person.move_to([-2.5, -2.5, 0])
        logic_passp.move_to([2, -2.5, 0])
        self.play(FadeTransform(person_copy, logic_person))
        self.wait(2)
        self.play(FadeTransform(passp_copy, logic_passp))
        self.wait(2)

        #Parte 3: Funde as entidades e relacionamento
        to_merge = VGroup(logic_person, logic_passp)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeTransform(to_merge, manage_merge))
        self.wait(2)
        self.play(manage_merge.animate.shift(RIGHT*3), anim, run_time= 2)
        self.wait()

        #Parte 4: Conclusao
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Eliminates the need for joints", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Simple implementation", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Hinders future expansions", color= BLACK, font_size= 32).next_to(cons, DOWN, buff= 0.25)
        con_2 = Tex(r"-Optional attributes may only apply \\to some records, resulting in lots of NULL values", color= BLACK, font_size= 32).next_to(con_1, DOWN, buff= 0.25)

        self.play(FadeOut(intro))
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(con_1))
        self.play(Write(con_2))
        self.wait(2)

class Attribute_Adding(Scene):
    def construct(self):
        #Parte 1: Introducao ao metodo
        relation.move_to([0, 0.75, 0])
        title = Tex("Method 2: Attribute adding", color= BLACK, font_size= 36).move_to([-4.8, 3.75, 0])
        desc = Tex("For this method, add the optional entity's attributes to the mandatory entity's table.", color= BLACK, font_size= 32).next_to(relation, UP, buff=1)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP*1.5), run_time= 2)
        self.play(Write(desc, run_time= 2))
        self.wait(3)

        #Parte 2: Transforma Person e Passport conceitual em logico    
        self.play(FadeOut(desc))
        self.play(relation.animate.shift(UP * 2))

        path = ArcBetweenPoints(start= person.get_center(), end= [-2, -2.5, 0], angle= 0.5)
        path2 = ArcBetweenPoints(start= passp.get_center(), end= [2, -1.5, 0], angle= -0.5)
        person_copy = person.copy()
        passp_copy = passp.copy()
        
        self.wait()
        self.play(MoveAlongPath(person_copy, path))
        self.wait()
        self.play(FadeTransform(person_copy, logic_person))
        self.wait(2)
        self.play(MoveAlongPath(passp_copy, path2))
        logic_passp.move_to(passp_copy.get_center())
        self.wait()
        self.play(FadeTransform(passp_copy, logic_passp))
        self.wait(2)

        # #Parte 3: Destacar atributos do relacionamento e adicionar ao modelo logico de person
        desc2 = Tex("In this particular case, the ID in Person and Passport are the same attributes, so nothing will be added!", color= BLACK, font_size= 32).next_to(relation, DOWN, SMALL_BUFF)
        
        self.play(Write(desc2, run_time= 3))
        self.wait(3)
        # passp_code = VGroup(passp_att, passp_att_con, passp_att_code)
        # path = ArcBetweenPoints(start= passp_code.get_center(), end= [-0.5, 0.5, 0], angle= -1.7)

        # column_copy = person_att_adding.get_columns()[2].copy()
        # column_copy.set_color(BLACK)
        # column_copy2 = person_att_adding.get_columns()[3].copy()
        # column_copy2.set_color(BLACK)
        # passp_code_copy = passp_code.copy()
        # passp_name_copy = passp_name.copy()

        # self.play(MoveAlongPath(passp_code_copy, path))
        # self.play(Circumscribe(passp_code_copy, Circle, fade_out= True, color= PURE_RED))
        # self.wait()
        # self.play(ReplacementTransform(passp_code_copy, column_copy))
        # person_att_adding.add_highlighted_cell((1, 3), color= ORANGE)
        # self.wait(2)

        # self.play(MoveAlongPath(passp_name_copy, path2))
        # self.play(Circumscribe(passp_name_copy, Circle, fade_out= True, color= PURE_RED))
        # self.wait()
        # self.play(ReplacementTransform(passp_name_copy, column_copy2))
        # person_att_adding.add_highlighted_cell((1, 4), color= ORANGE)
        # self.wait(2)

        #Parte 4: Representar o relacionamento pela chave estrangeira
        exp = Tex("The relationship will be represented as a Foreign Key between Employee's and Department's table:", color= BLACK, font_size= 32).next_to(desc2, DOWN)
        manage_copy = manage.copy()
        manage_copy.generate_target()
        manage_copy.target.next_to(manage, DOWN, 2)#.scale(0.8)
        
        line = Line(start= [-4.1, 0, 0], end= [0.75, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [0.85, -0.1, 0], end= [0.85, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        fk = VGroup(line, arco, arco2, line2, line3)
        table_group = VGroup(logic_passp, logic_person)
        fk.move_to(table_group.get_top()).shift(UP*0.25)
        key = Tex("FK", color= PURE_RED, font_size= 38).next_to(fk, UP, SMALL_BUFF)

        self.play(Write(exp))
        self.wait(2)
        self.play(MoveToTarget(manage_copy))
        self.wait(2)
        self.play(ReplacementTransform(manage_copy, fk))
        self.wait()
        self.play(Write(key))
        self.wait()

        #Parte 5: Conclusao
        final = VGroup(fk, key, logic_person, logic_passp)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Easy implementation", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Model is extendable", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        pro_3 = Tex("-No null-values tuples", color= BLACK, font_size= 32).next_to(pro_2, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Joints necessary for searches.", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeOut(exp, desc2))
        self.play(final.animate.scale(0.75))
        self.play(final.animate.shift(RIGHT*3.5), anim, run_time= 3)
        self.wait()
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(pro_3))
        self.play(Write(con_1))
        self.wait(2)

class New_Relation(Scene):
    def construct(self):
        #Parte 1: apresentacao do metodo de nova relacao
        relation.move_to([0, 1, 0])
        title = Tex("Method 3: New Relation", color= BLACK, font_size= 36).move_to([-4.8, 3.7, 0])
        desc = Tex("For this method, the entities will have their own separated tables.", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        logic_person.move_to([[-3.5, -2.45, 0]])
        logic_passp.move_to([[4, -1.9, 0]])
        path = ArcBetweenPoints(start= person.get_center(), end= logic_person.get_center(), angle= 1.7)
        path2 = ArcBetweenPoints(start= passp.get_center(), end= logic_passp.get_center(), angle= -1.7)
        person_copy = person.copy()
        passp_copy = passp.copy()

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.play(Write(desc))
        self.wait(3)
        self.play(MoveAlongPath(person_copy, path))
        self.wait()
        self.play(FadeTransform(person_copy, logic_person))
        self.wait()
        self.play(MoveAlongPath(passp_copy, path2))
        self.wait()
        self.play(FadeTransform(passp_copy, logic_passp))
        self.wait(2)

        #Parte 2: Transformacao da table de relacao
        to_elim = VGroup(desc)
        desc = Tex("The relationship will also have its own table:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        logic_manage.shift(UP*0.1)
        path = Line(manage.get_center(), logic_manage.get_center())
        manage_copy = manage.copy()

        self.play(FadeOut(to_elim))
        self.wait(2)
        self.play(Write(desc))
        self.wait(2)
        self.play(MoveAlongPath(manage_copy, path))
        self.wait(2)
        self.play(FadeTransform(manage_copy, logic_manage))
        self.wait()

        #Parte 3: Destaca as chaves primárias
        to_elim = VGroup(desc)
        desc = Tex("Note that the relationship's table is comprised by the primary keys of the entities:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        id = VGroup(person_att, person_att_code, person_att_con)
        code = VGroup(passp_att, passp_att_code, passp_att_con)
        box_pk = SurroundingRectangle(id, corner_radius= 0.25, buff= 0.2, color= PURE_RED)
        arr_pk = CurvedArrow(start_point= box_pk.get_bottom(), end_point= logic_manage.get_entries([1, 1]).get_left(), color= PURE_RED, angle= PI/4)
        box_pk2 = SurroundingRectangle(code, corner_radius= 0.25, buff= 0.2, color= PURE_RED)
        arr_pk2 = CurvedArrow(start_point= box_pk2.get_bottom(), end_point= logic_manage.get_entries([1, 2]).get_right(), color= PURE_RED, angle= -PI/4)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(desc))
        self.wait()
        self.play(Create(box_pk), Create(box_pk2))
        self.wait()
        self.play(Create(arr_pk), Create(arr_pk2))
        self.wait(2)

        #Parte 4: Destaca as chaves estrangeiras
        to_elim = VGroup(desc, box_pk, box_pk2, arr_pk, arr_pk2)
        desc = Tex("Next, the primary key of each entity will be a foreign key to the relationship's table.", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        table_group = VGroup(logic_person, logic_manage)
        table_group2 = VGroup(logic_passp, logic_manage)
        line = Line(start= [-4.1, 0, 0], end= [-1, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [-0.9, -0.1, 0], end= [-0.9, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        fk = VGroup(line, arco, arco2, line2, line3)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT)
        fk2 = fk.copy()
        fk2.move_to(table_group2.get_top()).shift(UP*0.25).shift(RIGHT)
        key = Tex("FK", color= PURE_RED, font_size= 38).next_to(fk, UP, SMALL_BUFF)
        key2 = key.copy().next_to(fk2, UP, SMALL_BUFF)

        self.play(FadeOut(to_elim))
        self.wait()
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

        #Parte 5: Conclusao
        final = VGroup(fk, fk2, key, key2, logic_person, logic_passp, logic_manage)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Nothing :(", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-More complicated searches.", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        con_2 = Tex("-Complex implementation", color= BLACK, font_size= 40).next_to(con_1, DOWN, buff= 0.25)
        con_3 = Tex("-Redundant data", color= BLACK, font_size= 40).next_to(con_2, DOWN, buff= 0.25)
        con_4 = Tex("-Higher number of tables", color= BLACK, font_size= 40).next_to(con_3, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeOut(desc))
        self.play(final.animate.scale(0.75))
        self.play(final.animate.shift(RIGHT*3.5), anim, run_time= 3)
        self.wait()
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(con_1))
        self.play(Write(con_2))
        self.play(Write(con_3))
        self.play(Write(con_4))
        self.wait(2)