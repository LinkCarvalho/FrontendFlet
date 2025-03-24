import flet as ft

def register(page):

    Senha = ft.Ref[ft.TextField]()  

    def toggle_password(e):
        senha_field = Senha.current  
        senha_field.password = not senha_field.password  
        senha_field.suffix.icon = ft.icons.VISIBILITY if senha_field.password else ft.icons.VISIBILITY_OFF
        page.update()

    def show_form(tipo):
        form_container.clean()  

        if tipo == "psicologo":
            form_container.content = psicologo_form()
        else:
            form_container.content = paciente_form()

        page.update()

    def psicologo_form():
        return ft.Column([
            ft.TextField(
                label="Código", 
                label_style=ft.TextStyle(color="black"),
                width=300, 
                border_color="black", 
                color="black", 
                bgcolor="white"
            ),
            ft.TextField(
                ref=Senha,  
                label="Senha", 
                label_style=ft.TextStyle(color="black"), 
                password=True,
                width=300,
                border_color="black",
                color="black",
                bgcolor="white",
                suffix=ft.IconButton(
                    icon=ft.icons.VISIBILITY_OFF,  
                    icon_color="black",
                    on_click=toggle_password
                )
            ),
            ft.ElevatedButton(
                "Registrar", 
                on_click= lambda e: print("Registrado!"),  
                width=150, 
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),  
                    elevation=5, 
                    overlay_color="rgba(255, 255, 255, 0.2)",
                    bgcolor="black",
                    color="white"
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def paciente_form():
        return ft.Column([
            ft.TextField(
                label="Código", 
                label_style=ft.TextStyle(color="black"),
                width=300, 
                border_color="black", 
                color="black", 
                bgcolor="white"
            ),
            ft.TextField(
                ref=Senha,  
                label="Senha", 
                label_style=ft.TextStyle(color="black"), 
                password=True,
                width=300,
                border_color="black",
                color="black",
                bgcolor="white",
                suffix=ft.IconButton(
                    icon=ft.icons.VISIBILITY_OFF,  
                    icon_color="black",
                    on_click=toggle_password
                )
            ),
            ft.ElevatedButton(
                "Registrar", 
                on_click= lambda e: print("Registrado!"),  
                width=150, 
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),  
                    elevation=5, 
                    overlay_color="rgba(255, 255, 255, 0.2)",
                    bgcolor="black",
                    color="white"
                )
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    form_container = ft.Container()

    return ft.View(
        route="/register",
        bgcolor="#f2dbc2", 
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Text("Escolha seu perfil:", size=20, weight="bold", color= "black"),
                    ft.Row([
                        ft.ElevatedButton("Sou Psicólogo", on_click=lambda e: show_form("psicologo"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),  
                                elevation=5, 
                                overlay_color="rgba(255, 255, 255, 0.2)",
                                bgcolor="black",
                                color="white"
                )),
                        ft.ElevatedButton("Sou Paciente", on_click=lambda e: show_form("paciente"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=5),  
                                elevation=5, 
                                overlay_color="rgba(255, 255, 255, 0.2)",
                                bgcolor="black",
                                color="white"
                )),
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
                    form_container,  
                    ft.ElevatedButton("Voltar ao Login", on_click=lambda e: page.go("/"), style= ft.ButtonStyle(color= "white"))
                ],
                alignment=ft.MainAxisAlignment.CENTER,  
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                expand=True  
            )
        ]
    )
