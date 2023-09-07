from tkinter import CENTER
from turtle import right
from manim import *

config.background_color = WHITE
config.max_files_cached = 500

#Bloco para o relacionamento Organize:
#---------------------------------------------------------------------------------------------------------------------------------------#
org_shape = Polygon([-1.1, 0, 0], [0, 1, 0], [1.1, 0, 0], [0, -1, 0], color = BLACK).move_to([0, 0, 0])
org_title = Text("Organizes", color = BLACK, font_size=24).move_to(org_shape.get_center())
org_att = Circle(radius = 0.1, color= BLACK, fill_opacity= 0).next_to(org_shape.get_bottom(), DOWN)
org_att_date = Text("Date", color= BLACK, font_size=15).next_to(org_att, DOWN, buff=0.1)
org_att_connect = Line(start= org_shape.get_bottom(), end= org_att.get_top(), color= BLACK)

org = VGroup(org_shape, org_title, org_att, org_att_date, org_att_connect)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Conferencia:
#---------------------------------------------------------------------------------------------------------------------------------------#
conf_title = Text("Conference", color = BLACK, font_size= 24)
conf_shape = SurroundingRectangle(conf_title, color = BLACK, buff = 0.4)
conf_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 1).next_to(conf_shape.get_bottom(), DL*1.5)
conf_att2 = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(conf_shape.get_bottom(), DOWN)
conf_att_code = Tex("ID", color= BLACK, font_size= 20).next_to(conf_att, DOWN, buff= 0.05)
conf_att_name = Tex("Name", color= BLACK, font_size= 20).next_to(conf_att2, DOWN, buff= 0.05)
conf_att_con = Line(start= [-0.475, -0.55, 0], end= conf_att.get_top(), color= BLACK)
conf_att_con2 = Line(start= conf_shape.get_bottom(), end= conf_att2.get_top(), color= BLACK)

conf = VGroup(conf_title, conf_shape, conf_att, conf_att_code, conf_att_con, conf_att2, conf_att_name, conf_att_con2)
#---------------------------------------------------------------------------------------------------------------------------------------#

#Bloco para a entidade Comissao:
#---------------------------------------------------------------------------------------------------------------------------------------#
com_title = Text("Comission", color = BLACK, font_size= 24)
com_shape = SurroundingRectangle(com_title, color = BLACK, buff = 0.4)
com_att = Circle(radius= 0.1, color= BLACK, fill_opacity= 0).next_to(com_shape.get_bottom(), DL*1.5)
com_att_code = Tex("Address", color= BLACK, font_size= 20).next_to(com_att, DOWN, buff= 0.05)
com_att_con = Line(start= [-0.475, -0.55, 0], end= com_att.get_top(), color= BLACK)

com = VGroup(com_title, com_shape, com_att, com_att_code, com_att_con)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(conf, org, com).arrange(buff= 1)
conf.shift(DOWN*0.035)
com.shift(DOWN*0.035)

#Relacoes entre os blocos:
#---------------------------------------------------------------------------------------------------------------------------------------#
conf_org_con = Line(start= conf_shape.get_right(), end= org_shape.get_left(), color= BLACK)
com_org_con = Line(start= com_shape.get_left(), end= org_shape.get_right(), color= BLACK)

relation_conectors = VGroup(conf_org_con, com_org_con)

com_org_cardi = Tex("(1, 1)", color= BLACK, font_size= 24).next_to(com_org_con, UP, buff=0.05)
conf_org_cardi = Tex("(1, 1)", color= BLACK, font_size= 24).next_to(conf_org_con, UP, buff=0.1)

cardinality = VGroup(com_org_cardi, conf_org_cardi)
#---------------------------------------------------------------------------------------------------------------------------------------#

relation = VGroup(relation, relation_conectors, cardinality).shift(DOWN).scale(0.6)


#Modelo logico da entidade Comissao:
#------------------------------------------------------------------------------------#
logic_com = Table(
    [["800 Sylvan Ave."],
    ["1230 Washington Ave."],
    ["416 Rowland St."],
    ["130 West Main St."],
    ["420 Free Road"],
    ["1520 Harrison Ave."]],
    col_labels=[Text("Address", color= BLACK)],
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([3, -1.75, 0])
logic_com.get_entries().set_color(BLACK)
logic_com.add_highlighted_cell((1, 1), color= ORANGE)
logic_com.scale(0.4)
#------------------------------------------------------------------------------------#

#Modelo logico da entidade Conferencia:
#---------------------------------------------------------------------------------------#
logic_conf = Table(
    [["Innovative Eng."],
    ["Bioinformatics"],
    ["Intelligent Control"],
    ["Radiology"],
    ["Nanotek Summit"],
    ["Smart Structures"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Name", color= BLACK)],
    top_left_entry=Text("ID", color= BLACK),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([-3, -1.75, 0])
logic_conf.get_entries().set_color(BLACK)
for item in range(2):
    logic_conf.add_highlighted_cell((1, item), color= ORANGE)
logic_conf.scale(0.4)
#---------------------------------------------------------------------------------------#

#Modelo logico do relacionamento Org:
#---------------------------------------------------------------------------------------#
logic_org = Table(
    [["03/10/2023"],
    ["11/06/2023"],
    ["12/02/2023"],
    ["05/09/2023"],
    ["01/04/2024"],
    ["05/07/2024"]],
    col_labels=[Text("Date", color= BLACK)],
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -1.75, 0])
logic_org.get_entries().set_color(BLACK)
logic_org.add_highlighted_cell((1, 1), color= ORANGE)
logic_org.scale(0.4)
#---------------------------------------------------------------------------------------#


#Modelo logico da organizacao na Fusao de Entidades
#---------------------------------------------------------------------------------------#
org_merge = Table(
    [["Innovative Eng.","800 Sylvan Ave.","03/10/2023"],
    ["Bioinformatics","1230 Washington Ave.", "11/06/2023"],
    ["Intelligent Control","416 Rowland St.", "12/02/2023"],
    ["Radiology","130 West Main St.", "05/09/2023"],
    ["Nanotek Summit","420 Free Road", "01/04/2024"],
    ["Smart Structures","1520 Harrison Ave.", "05/07/2024"]],
    row_labels=[Text("01"), Text("02"), Text("03"), Text("04"), Text("05"), Text("06")],
    col_labels=[Text("Address"), Text("Name"), Text("Date")],
    top_left_entry=Text("ID"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -1.75, 0])
org_merge.get_entries().set_color(BLACK)
for item in range(4):
    org_merge.add_highlighted_cell((1, item), color= ORANGE)
org_merge.scale(0.4)
#---------------------------------------------------------------------------------------#

#Modelo logico de Organiza em Adicao de Atributos
#---------------------------------------------------------------------------------------#
org_adding = Table(
    [["03/10/2023","01"],
    ["11/06/2023","02"],
    ["12/02/2023","03"],
    ["05/09/2023","04"],
    ["01/04/2024","05"],
    ["05/07/2024","06"]],
    row_labels=[Text("800 Sylvan Ave."), Text("1230 Washington Ave."), Text("416 Rowland St."), Text("130 West Main St."), Text("420 Free Road"), Text("1520 Harrison Ave.")],
    col_labels=[Text("Conf_Date"), Text("Conf_ID")],
    top_left_entry=Text("Address"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6)
org_adding.get_columns()[0].set_color(BLACK)
org_adding.add_highlighted_cell((1, 1), color= ORANGE)
org_adding.scale(0.35)
#---------------------------------------------------------------------------------------#

#Modelo logico de Organiza em Relacionamento Proprio
#---------------------------------------------------------------------------------------#
org_new = Table(
    [["01","800 Sylvan Ave."],
    ["02","1230 Washington Ave."],
    ["03","416 Rowland St."],
    ["04","130 West Main St."],
    ["05","420 Free Road"],
    ["06","1520 Harrison Ave."]],
    row_labels=[Text("03/10/2023"), Text("11/06/2023"), Text("12/02/2023"), Text("05/09/2023"), Text("01/04/2024"), Text("05/07/2024")],
    col_labels=[Text("Conf_ID"), Text("Com_Address")],
    top_left_entry=Text("Date"),
    include_outer_lines=True,
    line_config= {"color": BLACK},
    v_buff=0.5, h_buff=0.6).move_to([0, -2, 0])
org_new.get_columns()[0].set_color(BLACK)
org_new.add_highlighted_cell((1, 1), color= ORANGE)
org_new.scale(0.375)
#---------------------------------------------------------------------------------------#

#Arquivo da animacao de introducao
class Introduction(Scene):
    def construct(self):
        #Parte 1: Introducao de 1:1 (ambos lados obrigatorios) e modelo exemplo
        intro = Tex("We create one-to-one mandatory relationships when one instance of an entity has a relationship with ONE instance from another entity.", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_2 = Tex("In the following case, both sides of the relationship are mandatory.", color= BLACK, font_size= 32).next_to(intro, DOWN, buff= 0.25)        
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
        intro_3 = Tex("MANDATORY One-to-One relationships are identified with cardinality 1 to 1 like this:", color= BLACK, font_size= 32).next_to(intro_2, DOWN, buff=0.5)

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(intro_3))
        self.wait(2)
        self.play(relation.animate.scale(1.5))
        for _ in range(3):  
            self.play(Indicate(cardinality, color= PURE_RED))
        self.wait(2)

        #Parte 3: Apresentacao dos metodos e inicio da fusao de entidade
        to_elim = VGroup(intro, intro_2, intro_3)
        intro = Tex("There are 3 ways to deal with One-To-One Mandatory relationships:", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)
        intro_2 = Tex("Method 1: Entity Fusion", color= BLACK, font_size= 36).next_to(intro, DOWN, buff= 0.5)
        intro_3 = Tex("Method 2: Attribute adding", color= BLACK, font_size= 36).next_to(intro_2, DOWN, buff= 0.5)
        intro_4 = Tex("Method 3: New relation", color= BLACK, font_size= 36).next_to(intro_3, DOWN, buff= 0.5)
        intro_final = Tex("Let's see how each one of those works!", color= BLACK, font_size= 32).next_to(relation, UP, buff=3)

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
        relation.move_to([0, 1, 0])
        title = Tex("Method 1: Entity Fusion", color= BLACK, font_size= 36).move_to([-5, 3.75, 0])
        intro = Tex("For this method, we are going to merge both entities and the relationship into a single table:", color= BLACK, font_size= 32).next_to(relation, UP, buff= 0.75)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.wait()
        self.play(Write(intro))
        self.wait(2)

        #Parte 2: Traz as entidades no modelo conceitual e transforma em logico
        conf_copy = conf.copy()
        com_copy = com.copy()
        org_copy = org.copy()
        arc = ArcBetweenPoints(start= conf.get_center(), end= [-3, -1.75, 0])
        arc2 = ArcBetweenPoints(start= com.get_center(), end= [3, -1.75, 0], angle= -PI/4)
        arc3 = Line(org.get_center(), [0, -1.75, 0])

        self.play(MoveAlongPath(conf_copy, arc))
        self.wait()
        self.play(MoveAlongPath(org_copy, arc3))
        self.wait()
        self.play(MoveAlongPath(com_copy, arc2))
        self.wait(2)
        self.play(FadeTransform(conf_copy, logic_conf))
        self.wait(2)
        self.play(FadeTransform(com_copy, logic_com))
        self.wait(2)
        self.play(FadeTransform(org_copy, logic_org))
        self.wait(2)

        #Parte 3: Funde as entidades e relacionamento
        to_merge = VGroup(logic_conf, logic_com, logic_org)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -2, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(FadeTransform(to_merge, org_merge))
        self.wait(4)
        self.play(org_merge.animate.shift(RIGHT*3), anim, run_time= 2)
        self.wait()

        #Parte 4: Conclusao
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Eliminates the need for joints", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Simple implementation", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        pro_3 = Tex("-No Null-valued tuples", color= BLACK, font_size= 32).next_to(pro_2, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Hinders future expansions", color= BLACK, font_size= 32).next_to(cons, DOWN, buff= 0.25)

        self.play(FadeOut(intro))
        self.play(Write(pros))
        self.play(Write(cons))
        self.play(Write(pro_1))
        self.play(Write(pro_2))
        self.play(Write(pro_3))
        self.play(Write(con_1))
        self.wait(2)

class Attribute_Adding(Scene):
    def construct(self):
        #Parte 1: Introducao ao metodo
        relation.move_to([0, 0.75, 0])
        title = Tex("Method 2: Attribute adding", color= BLACK, font_size= 36).move_to([-4.8, 3.75, 0])
        desc = Tex("For this method, add the attributes from one entity to the other one.", color= BLACK, font_size= 32).next_to(relation, UP, buff=1)
        desc2 = Tex("In this case, as both are mandatory, the adding can be done either way.", color= BLACK, font_size= 32).next_to(desc, DOWN, buff=0.25)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP*1.5), run_time= 2)
        self.play(Write(desc, run_time= 2))
        self.wait()
        self.play(Write(desc2))
        self.wait(3)

        #Parte 2: Transforma Conferencia e Comissao conceitual em logico
        to_elim = VGroup(desc, desc2)

        self.play(FadeOut(to_elim))
        self.play(relation.animate.shift(UP * 2))

        path = ArcBetweenPoints(start= conf.get_center(), end= [-3.5, -1.6, 0], angle= 0.5)
        path2 = ArcBetweenPoints(start= com.get_center(), end= [2.25, -1.5, 0], angle= -0.5)
        conf_copy = conf.copy()
        com_copy = com.copy()
        
        self.wait()
        self.play(MoveAlongPath(conf_copy, path))
        logic_conf.move_to(conf_copy.get_center())
        self.wait()
        self.play(FadeTransform(conf_copy, logic_conf))
        self.wait(2)
        self.play(MoveAlongPath(com_copy, path2))
        org_adding.move_to(com_copy.get_center())
        self.wait()
        self.play(FadeTransform(com_copy, org_adding))
        self.wait(2)

        #Parte 3: Destacar atributos de Conferencia e adicionar ao modelo logico de Comissao
        date = VGroup(org_att, org_att_connect, org_att_date)
        path_end = Point(org_adding.get_columns()[1].get_top()).shift(UP*0.5)
        path_date = ArcBetweenPoints(start= date.get_center(), end= path_end.get_center(), angle= PI/4)
        column_date_copy = org_adding.get_columns()[1].copy()
        column_date_copy.set_color(BLACK)
        date_copy = date.copy()

        id = VGroup(conf_att, conf_att_con, conf_att_code)
        path_end = Point(org_adding.get_columns()[2].get_top()).shift(UP*0.5)
        path_id = ArcBetweenPoints(start= id.get_center(), end= path_end.get_center(), angle= PI/4)
        column_id_copy = org_adding.get_columns()[2].copy()
        column_id_copy.set_color(BLACK)
        id_copy = id.copy()

        self.play(Circumscribe(date, Circle, fade_out= True, color= PURE_RED))
        self.play(MoveAlongPath(date_copy, path_date))
        self.wait()
        self.play(ReplacementTransform(date_copy, column_date_copy))
        org_adding.add_highlighted_cell((1, 2), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(id, Circle, fade_out= True, color= PURE_RED))
        self.play(MoveAlongPath(id_copy, path_id))
        self.wait()
        self.play(ReplacementTransform(id_copy, column_id_copy))
        org_adding.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        #Parte 4: Representar o relacionamento pela chave estrangeira
        exp = Tex("The relationship will be represented as a Foreign Key between Conference's and Comission's table:", color= BLACK, font_size= 32).next_to(relation, DOWN)
        organize = VGroup(org_shape, org_title)
        org_copy = organize.copy()
        org_copy.generate_target()
        org_copy.target.next_to(org, DOWN)#.scale(0.8)
        
        line = Line(start= [-4.4, 0, 0], end= [4.5, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [4.6, -0.1, 0], end= [4.6, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.5, -0.1, 0], end= [-4.5, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        fk = VGroup(line, arco, arco2, line2, line3)
        table_group = VGroup(logic_conf, org_adding)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT*0.15)
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
        final = VGroup(fk, key, logic_conf, org_adding, column_id_copy, column_date_copy)
        pros = Tex("Pros:", color= PURE_GREEN, font_size= 40).move_to([-3, 3, 0])
        pro_1 = Tex("-Easy implementation", color= BLACK, font_size= 32).next_to(pros, DOWN, buff= 0.25)
        pro_2 = Tex("-Model is extendable", color= BLACK, font_size= 32).next_to(pro_1, DOWN, buff= 0.25)
        pro_3 = Tex("-No null-values tuples", color= BLACK, font_size= 32).next_to(pro_2, DOWN, buff= 0.25)
        cons = Tex("Cons:", color= PURE_RED, font_size= 40).move_to([3, 3, 0])
        con_1 = Tex("-Joints necessary for searches.", color= BLACK, font_size= 40).next_to(cons, DOWN, buff= 0.25)
        arc = ArcBetweenPoints(start= relation.get_center(), end= [-4, -1.5, 0])
        anim = MoveAlongPath(relation, arc)

        self.play(final.animate.scale(0.65))
        self.play(final.animate.shift(RIGHT*3), anim, run_time= 3)
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
        logic_conf.move_to([[-4.5, -2, 0]])
        logic_com.move_to([[4.5, -2, 0]]).scale(0.96)
        path = ArcBetweenPoints(start= conf.get_center(), end= logic_conf.get_center(), angle= 1.7)
        path2 = ArcBetweenPoints(start= com.get_center(), end= logic_com.get_center(), angle= -1.7)
        conf_copy = conf.copy()
        com_copy = com.copy()

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(relation, shift= UP), run_time= 2)
        self.play(Write(desc))
        self.wait(3)
        self.play(MoveAlongPath(conf_copy, path))
        self.wait()
        self.play(FadeTransform(conf_copy, logic_conf))
        self.wait()
        self.play(MoveAlongPath(com_copy, path2))
        self.wait()
        self.play(FadeTransform(com_copy, logic_com))
        self.wait(2)

        #Parte 2: Transformacao da table de relacao
        to_elim = VGroup(desc)
        desc = Tex("The relationship will also have its own table:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)
        path = Line(org.get_center(), org_new.get_center())
        manage_copy = org.copy()

        self.play(FadeOut(to_elim))
        self.wait(2)
        self.play(Write(desc))
        self.wait(2)
        self.play(MoveAlongPath(manage_copy, path))
        self.wait(2)
        self.play(FadeTransform(manage_copy, org_new))
        self.wait()

        #Parte 3: Destaca as chaves primárias
        to_elim = VGroup(desc)
        desc = Tex("The relationship's table will be comprised by the primary keys (if any) of the involved entities:", color= BLACK, font_size= 32).next_to(relation, UP, buff=0.5)      

        self.play(FadeOut(to_elim))
        self.wait()
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(desc))
        self.wait()
        self.play(relation.animate.shift(UP*1.5))
        self.wait()

        id = VGroup(conf_att, conf_att_con, conf_att_code)
        path_end = Point(org_new.get_columns()[1].get_top()).shift(UP*0.5)
        path_id = ArcBetweenPoints(start= id.get_center(), end= path_end.get_center(), angle= PI/4)
        column_id_copy = org_new.get_columns()[1].copy()
        column_id_copy.set_color(BLACK)
        id_copy = id.copy()

        address = VGroup(com_att, com_att_code, com_att_con)
        path_end_ad = Point(org_new.get_columns()[2].get_top()).shift(UP*0.5)
        path_address = ArcBetweenPoints(start= address.get_center(), end= path_end_ad.get_center(), angle= -PI/4)
        column_ad_copy = org_new.get_columns()[2].copy()
        column_ad_copy.set_color(BLACK)
        address_copy = address.copy()  
        
        self.play(Circumscribe(id, Circle, fade_out= True, color= PURE_RED))
        self.play(MoveAlongPath(id_copy, path_id))
        self.wait()
        self.play(ReplacementTransform(id_copy, column_id_copy))
        org_new.add_highlighted_cell((1, 2), color= ORANGE)
        self.wait(2)

        self.play(Circumscribe(address, Circle, fade_out= True, color= PURE_RED))
        self.play(MoveAlongPath(address_copy, path_address))
        self.wait()
        self.play(ReplacementTransform(address_copy, column_ad_copy))
        org_new.add_highlighted_cell((1, 3), color= ORANGE)
        self.wait(2)

        #Parte 4: Destaca as chaves estrangeiras
        desc = Tex("Next, the primary key of each entity will be a foreign key to the relationship's table.", color= BLACK, font_size= 30).next_to(relation, DOWN, buff=0.5)
        table_group = VGroup(logic_conf, org_new)
        table_group2 = VGroup(logic_com, org_new)

        line = Line(start= [-4.1, 0, 0], end= [1, 0, 0]).set_color(PURE_RED)
        line2= Arrow(start= [1.1, -0.1, 0], end= [1.1, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line3= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco = ArcBetweenPoints(start= line.get_end(), end= line2.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco2 = ArcBetweenPoints(start= line.get_start(), end= line3.get_start()).set_color(PURE_RED)
        
        line4 = Line(start= [-4.1, 0, 0], end= [-1, 0, 0]).set_color(PURE_RED)
        line5= Arrow(start= [-0.9, -0.1, 0], end= [-0.9, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        line6= Arrow(start= [-4.2, -0.1, 0], end= [-4.2, -0.47, 0], max_stroke_width_to_length_ratio= 10, max_tip_length_to_length_ratio= 0.5).set_color(PURE_RED)
        arco3 = ArcBetweenPoints(start= line4.get_end(), end= line5.get_start(), angle = - PI/2).set_color(PURE_RED)
        arco4 = ArcBetweenPoints(start= line4.get_start(), end= line6.get_start()).set_color(PURE_RED)

        fk = VGroup(line, arco, arco2, line2, line3)
        fk.move_to(table_group.get_top()).shift(UP*0.25).shift(LEFT*1.4)

        fk2 = VGroup(line4, arco3, arco4, line5, line6)
        fk2.move_to(table_group2.get_top()).shift(UP*0.25).shift(RIGHT*1.5)
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
        final = VGroup(fk, fk2, key, key2, logic_conf, logic_com, org_new, column_ad_copy, column_id_copy)
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
