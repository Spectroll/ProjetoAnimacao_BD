from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

# WORK -> ORG || CONF -> DEPT || COM -> EMP

#Bloco para o relacionamento Work:
#---------------------------------------------------------------------------------------------------------------------------------------#
work_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
work_title = Text("Works", color = BLACK, font_size=24).move_to(work_shape.get_center())
work_att = Circle(radius = 0.1, color= BLACK, fill_opacity= 0).next_to(work_shape.get_bottom(), DOWN)
work_att_date = Text("Date", color= BLACK, font_size=15).next_to(work_att, DOWN, buff=0.1)
work_att_connect = Line(start= work_shape.get_bottom(), end= work_att.get_top(), color= BLACK)

work = VGroup(work_shape, work_title, work_att, work_att_date, work_att_connect)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Departamento:
#---------------------------------------------------------------------------------------------------------------------------------------#
dept_title = Text("Department", color = BLACK, font_size= 24)
dept_shape = SurroundingRectangle(dept_title, color = BLACK, buff = 0.4)
dept_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(dept_shape.get_bottom(), DL*1.5)
dept_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(dept_shape.get_bottom(), DOWN)
dept_att_code = Tex("Code", color= BLACK, font_size= 20).next_to(dept_att, DOWN, buff= 0.05)
dept_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(dept_att2, DOWN, buff= 0.05)
dept_att_con = Line(start= [-0.475, -0.55, 0], end= dept_att.get_top(), color= BLACK)
dept_att_con2 = Line(start= dept_shape.get_bottom(), end= dept_att2.get_top(), color= BLACK)

dept = VGroup(dept_title, dept_shape, dept_att, dept_att_code, dept_att_con, dept_att2, dept_att_name, dept_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Empregado:
#---------------------------------------------------------------------------------------------------------------------------------------#
emp_title = Text("Employee", color = BLACK, font_size= 24)
emp_shape = SurroundingRectangle(emp_title, color = BLACK, buff = 0.4)
emp_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(emp_shape.get_bottom(), DL*1.5)
emp_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(emp_shape.get_bottom(), DOWN)
emp_att_code = Tex("ID", color= BLACK, font_size= 20).next_to(emp_att, DOWN, buff= 0.05)
emp_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(emp_att2, DOWN, buff= 0.05)
emp_att_con = Line(start= [-0.475, -0.55, 0], end= emp_att.get_top(), color= BLACK)
emp_att_con2 = Line(start= emp_shape.get_bottom(), end= emp_att2.get_top(), color= BLACK)

emp = VGroup(emp_title, emp_shape, emp_att, emp_att_code, emp_att_con, emp_att2, emp_att_name, emp_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(dept, work, emp).arrange(buff= 1)
dept.shift(DOWN*0.035)
emp.shift(DOWN*0.035)

#Relacoes entre os blocos:
#---------------------------------------------------------------------------------------------------------------------------------------#
dept_work_con = Line(start= dept_shape.get_right(), end= work_shape.get_left(), color= BLACK)
emp_work_con = Line(start= emp_shape.get_left(), end= work_shape.get_right(), color= BLACK)

relation_conectors = VGroup(dept_work_con, emp_work_con)

emp_work_cardi = Tex("(0, N)", color= BLACK, font_size= 24).next_to(emp_work_con, UP, buff=0.05)
dept_work_cardi = Tex("(1, 1)", color= BLACK, font_size= 24).next_to(dept_work_con, UP, buff=0.1)

cardinality = VGroup(emp_work_cardi, dept_work_cardi)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(relation, relation_conectors, cardinality).shift(DOWN).scale(0.6)

#Modelo logico da entidade Empregado:
#------------------------------------------------------------------------------------#
logic_emp = Table(
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
    v_buff=0.5, h_buff=0.6)
logic_emp.get_entries().set_color(BLACK)
for item in range(2):
    logic_emp.add_highlighted_cell((1, item), color= ORANGE)
logic_emp.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da entidade Departamento:
#------------------------------------------------------------------------------------#
logic_dept = Table(
    [["Finance"],
    ["Marketing"],
    ["Comercial"],
    ["Human Resources"],
    ["Administrative"],
    ["Operations"]],
    row_labels=[Text("101"), Text("102"), Text("103"), Text("104"), Text("105"), Text("106")],
    col_labels=[Text("Name")],
    top_left_entry=Text("ID"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
logic_dept.get_entries().set_color(BLACK)
for item in range(2):
    logic_dept.add_highlighted_cell((1, item), color= ORANGE)
logic_dept.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da relacao em adicao de atributos:
#------------------------------------------------------------------------------------#
work_adding = Table(
   [["Veronica", "101", "Finance", "08/08/2008"],
    ["Roger", "102", "Marketing", "09/08/2009"],
    ["Elisa", "103", "Comercial", "10/02/2009"],
    ["Billy", "104", "Human Resources", "05/12/2008"],
    ["Adam", "105", "Administrative", "03/05/2015"],
    ["Alex", "106", "Operations", "09/01/2015"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name"), Text("Dept_ID"), Text("Dept_Name"), Text("Date")],
    top_left_entry=Text("ID"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
for item in range(2):
    work_adding.add_highlighted_cell((1, item+1), color= ORANGE)
    work_adding.get_columns()[item].set_color(BLACK)
work_adding.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da relacao em New Relation:
#------------------------------------------------------------------------------------#
work_new = Table(
   [["101", "01"],
    ["102", "02"],
    ["103", "03"],
    ["104", "04"],
    ["105", "05"],
    ["106", "06"]],
    row_labels=[Text("08/08/2008"), Text("09/08/2009"), Text("10/02/2009"), Text("05/12/2008"), Text("03/05/2015"), Text("09/01/2015")],
    col_labels=[Text("Dept_ID"), Text("Emp_ID")],
    top_left_entry=Text("Date"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
work_new.add_highlighted_cell((1, 1), color= ORANGE)
work_new.get_columns()[0].set_color(BLACK)
work_new.scale(0.4)
#------------------------------------------------------------------------------------#


#Arquivo da animacao de introducao
class Introduction(Scene):
    def construct(self):
        #Parte 1: Introducao de 1:N e modelo exemplo
        intro = Tex("We create one-to-many relationships when one instance of an entity has a relationship with many instances from another entity.", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_2 = Tex("In the following case, one side of the relationship is (0, N), which means the relation is optional.", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= 0.25)        
        intro_3 = Tex("Take this Entity-Relationship Diagram as example:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff= 0.25)

        self.play(Write(intro), run_time= 3)
        self.wait(4)
        self.play(Write(intro_2), run_time= 3)
        self.wait(4)
        self.play(Write(intro_3))
        self.wait(2)
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait(3)

        #Parte 2: Indicar cardinalidade (1:1)
        to_elim = VGroup(intro_3)
        intro_3 = Tex("Optional one-to-many relationships are identified with cardinality 0 to N like this:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff=0.5)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(intro_3))
        self.wait(2)
        self.play(relation.animate.shift(DOWN*0.5).scale(1.75))
        for _ in range(3):  
            self.play(Indicate(emp_work_cardi, color= PURE_RED))
        self.wait(2)

        #Parte 3: Apresentacao dos metodos e inicio da fusao de entidade
        to_elim = VGroup(intro, intro_2, intro_3)
        intro = Tex("There are 2 ways to deal with One-To-Many relationships:", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_3 = Tex("Method 1: Attribute adding", color= BLACK, font_size= 36).next_to(intro, DOWN, buff= 0.5)
        intro_4 = Tex("Method 2: New relation", color= BLACK, font_size= 36).next_to(intro_3, DOWN, buff= 0.5)
        intro_final = Tex("Let's see how each one of those works!", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)

        self.play(FadeOut(to_elim))
        self.play(Write(intro))
        self.wait(2)
        self.play(Write(intro_3))
        self.play(Write(intro_4))
        self.wait(2)
        self.play(FadeOut(intro))
        self.play(Write(intro_final))
        self.wait(5)


class Attribute_Adding(Scene):
    def construct(self):
        #Parte 1: Introducao ao metodo
        relation.move_to([0, 0.75, 0])
        title = Tex("Method 1: Attribute adding", color= BLACK, font_size= 36).move_to([-4.8, 3.75, 0])
        desc = Tex("For this method, add the attributes from one entity to the other one.", color= BLACK, font_size= 32).next_to(relation, UP, buff=1.25)
        desc2 = Tex("In this case, the attributes from the cardinality (1,1) entity will be added to the cardinality (0, N) entity.", color= BLACK, font_size= 32).next_to(desc, DOWN, buff=0.25)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP*1.5), run_time= 2)
        self.play(Write(desc, run_time= 2))
        self.wait(2)
        self.play(Write(desc2))
        self.wait(3)

        #Parte 2: Transforma Conferencia e Comissao conceitual em logico
        to_elim = VGroup(desc, desc2)

        self.play(FadeOut(to_elim))
        self.play(relation.animate.shift(UP * 2))

        path = ArcBetweenPoints(start= dept.get_center(), end= [-3.5, -1.6, 0], angle= 0.5)
        path2 = ArcBetweenPoints(start= emp.get_center(), end= [2.25, -1.5, 0], angle= -0.5)
        dept_copy = dept.copy()
        emp_copy = emp.copy()
        
        self.wait()
        self.play(MoveAlongPath(dept_copy, path))
        logic_dept.move_to(dept_copy.get_center())
        self.wait()
        self.play(FadeTransform(dept_copy, logic_dept))
        self.wait(2)
        self.play(MoveAlongPath(emp_copy, path2))
        work_adding.move_to(emp_copy.get_center()).shift(DOWN*0.1).shift(LEFT*0.5).scale(0.92)
        self.wait()
        self.play(FadeTransform(emp_copy, work_adding))
        self.wait(2)

        #Parte 3: Destacar atributos de Departamento e adicionar ao modelo logico de Empregado
        id = VGroup(dept_att, dept_att_con, dept_att_code)
        path_end = Point(work_adding.get_columns()[2].get_top()).shift(UP*0.5)
        path_id = ArcBetweenPoints(start= id.get_center(), end= path_end.get_center(), angle= PI/4)
        column_id_copy = work_adding.get_columns()[2].copy()
        column_id_copy.set_color(BLACK)
        id_copy = id.copy()

        name = VGroup(dept_att2, dept_att_con2, dept_att_name)
        path_end_name = Point(work_adding.get_columns()[3].get_top()).shift(UP*0.5)
        path_name = ArcBetweenPoints(name.get_center(), end= path_end_name.get_center(), angle = PI/4)
        column_name_copy = work_adding.get_columns()[3].copy()
        column_name_copy.set_color(BLACK)
        name_copy = name.copy()

        date = VGroup(work_att_date, work_att, work_att_connect)
        path_end_date = Point(work_adding.get_columns()[4].get_top()).shift(UP*0.5)
        path_date = ArcBetweenPoints(date.get_center(), end= path_end_date.get_center(), angle = PI/4)
        column_date_copy = work_adding.get_columns()[4].copy()
        column_date_copy.set_color(BLACK)
        date_copy = date.copy()

        self.play(Circumscribe(id, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(id_copy, path_id))
        self.wait()
        self.play(ReplacementTransform(id_copy, column_id_copy))
        work_adding.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(name, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(name_copy, path_name))
        self.wait()
        self.play(ReplacementTransform(name_copy, column_name_copy))
        work_adding.add_highlighted_cell((1, 4), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(date, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(date_copy, path_date))
        self.wait()
        self.play(ReplacementTransform(date_copy, column_date_copy))
        work_adding.add_highlighted_cell((1, 5), color= ORANGE)
        self.wait(2)

        #Parte 4: Representar o relacionamento pela chave estrangeira
        exp = Tex("The relationship will be represented as a Foreign Key between Department's and Employee's table:", color= BLACK, font_size= 32).next_to(relation, DOWN)
        organize = VGroup(work_shape, work_title)
        org_copy = organize.copy()
        org_copy.generate_target()
        org_copy.target.next_to(work, DOWN)#.scale(0.8)
        
        line = Line(start= [-4.3, 0, 0], end= [1, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [1.1, -0.1, 0], end= [1.1, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.4, -0.1, 0], end= [-4.4, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        fk = VGroup(line, arco, arco2, line2, line3)
        table_group = VGroup(logic_dept, work_adding)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT*2)
        key = Tex("FK", color= PURE_RED, font_size= 38).next_to(fk, UP, SMALL_BUFF)

        self.play(Write(exp))
        self.wait(3)
        self.play(FadeOut(exp))
        self.wait(2)
        self.play(MoveToTarget(org_copy))
        self.wait(2)
        self.play(ReplacementTransform(org_copy, fk))
        self.wait()
        self.play(Write(key))
        self.wait()

        #Parte 5: Conclusao
        final = VGroup(fk, key, logic_dept, work_adding, column_name_copy, column_id_copy, column_date_copy)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Enables future expansions.", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Simple implementation.", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-May be sparse", color= BLACK, font_size= 32).next_to(cons, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -1.75, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(final.animate.scale(0.65))
        self.play(final.animate.shift(RIGHT*3), anim, run_time= 3)
        self.wait()
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(con_1))
        self.wait(2)


class New_Relation(Scene):
    def construct(self):
        #Parte 1: apresentacao do metodo de nova relacao
        relation.move_to([0, 1, 0])
        title = Tex("Method 3: New Relation", color= BLACK, font_size= 36).move_to([-4.8, 3.7, 0])
        desc = Tex("For this method, the entities will have their own separated tables.", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        logic_dept.move_to([[-4.5, -2, 0]])
        logic_emp.move_to([[4.5, -2, 0]])
        path = ArcBetweenPoints(start= dept.get_center(), end= logic_dept.get_center(), angle= 1.7)
        path2 = ArcBetweenPoints(start= emp.get_center(), end= logic_emp.get_center(), angle= -1.7)
        dept_copy = dept.copy()
        emp_copy = emp.copy()

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.play(Write(desc))
        self.wait(3)
        self.play(MoveAlongPath(dept_copy, path))
        self.wait()
        self.play(FadeTransform(dept_copy, logic_dept))
        self.wait()
        self.play(MoveAlongPath(emp_copy, path2))
        self.wait()
        self.play(FadeTransform(emp_copy, logic_emp))
        self.wait(2)

        #Parte 2: Transformacao da table de relacao
        to_elim = VGroup(desc)
        desc = Tex("The relationship will also have its own table:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        work_new.move_to([0, -2, 0]).scale(0.925)
        path = Line(work.get_center(), work_new.get_center())
        work_copy = work.copy()

        self.play(FadeOut(to_elim))
        self.wait(2)
        self.play(Write(desc))
        self.wait(2)
        self.play(MoveAlongPath(work_copy, path))
        self.wait(2)
        self.play(FadeTransform(work_copy, work_new))
        self.wait()

        #Parte 3: Destaca as chaves primárias
        to_elim = VGroup(desc)
        desc = Tex("The relationship's table will be comprised by the primary keys of the involved entities:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)      

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(desc))
        self.wait()
        self.play(relation.animate.shift(UP*1.5))
        self.wait()

        dept_id = VGroup(dept_att, dept_att_con, dept_att_code)
        path_end = Point(work_new.get_columns()[1].get_top()).shift(UP*0.5)
        path_dept_id = ArcBetweenPoints(start= dept_id.get_center(), end= path_end.get_center(), angle= PI/4)
        column_dept_id_copy = work_new.get_columns()[1].copy()
        column_dept_id_copy.set_color(BLACK)
        dept_id_copy = dept_id.copy()

        emp_id = VGroup(emp_att, emp_att_code, emp_att_con)
        path_end_emp = Point(work_new.get_columns()[2].get_top()).shift(UP*0.5)
        path_address = ArcBetweenPoints(start= emp_id.get_center(), end= path_end_emp.get_center(), angle= -PI/4)
        column_emp_id_copy = work_new.get_columns()[2].copy()
        column_emp_id_copy.set_color(BLACK)
        emp_id_copy = emp_id.copy()  

        self.play(Circumscribe(dept_id, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(dept_id_copy, path_dept_id))
        self.wait()
        self.play(ReplacementTransform(dept_id_copy, column_dept_id_copy))
        work_new.add_highlighted_cell((1, 2), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(emp_id, Circle, fade_out= True, color= PURE_RED, run_time= 2))
        self.play(MoveAlongPath(emp_id_copy, path_address))
        self.wait()
        self.play(ReplacementTransform(emp_id_copy, column_emp_id_copy))
        work_new.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        #Parte 4: Destaca as chaves estrangeiras
        desc = Tex("Next, the primary key of each entity will be a foreign key to the relationship's table.", color= BLACK, font_size= 30).next_to(relation, DOWN, buff=0.5)
        table_group = VGroup(logic_emp, work_new)
        table_group2 = VGroup(logic_dept, work_new)

        line = Line(start= [-4.9, 0, 0], end= [0.8, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [0.9, -0.1, 0], end= [0.9, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-5, -0.1, 0], end= [-5, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        
        line4 = Line(start= [-3.5, 0, 0], end= [-1.2, 0, 0]).set_color(PURE_RED)
        line5= Arrow(start= [-1.1, -0.1, 0], end= [-1.1, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line6= Arrow(start= [-3.6, -0.1, 0], end= [-3.6, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco3 = ArcBetweenPoints(start= line4.get_end(), end= line5.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco4 = ArcBetweenPoints(start= line4.get_start(), end= line6.get_start()).set_color(PURE_RED)

        fk = VGroup(line, arco, arco2, line2, line3)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT*4.4)

        fk2 = VGroup(line4, arco3, arco4, line5, line6)
        fk2.move_to(table_group2.get_top()).shift(UP*0.25).shift(RIGHT*4.6)
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

        #Parte 5: Conclusao
        final = VGroup(fk, fk2, key, key2, logic_dept, logic_emp, work_new, column_emp_id_copy, column_dept_id_copy)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Enables future expansions.", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Higher amount of junctions", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        con_2 = Tex("-Higher amount of tables", color= BLACK, font_size= 40).next_to(con_1, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeOut(desc))
        self.play(final.animate.scale(0.65))
        self.play(final.animate.shift(RIGHT*3), anim, run_time= 3)
        self.wait()
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(con_1))
        self.play(Write(con_2))
        self.wait(2)