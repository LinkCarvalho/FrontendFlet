import flet as ft

def login(page):
    page.title = 'PsiMar'
    page.clean()
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True  

  
    def toggle_password(e):
        Senha.password = not Senha.password  
        Senha.suffix.icon = ft.icons.VISIBILITY if Senha.password else ft.icons.VISIBILITY_OFF
        page.update()

    def login_action(e):
        if not Usuario.value:
            Usuario.error_text = "Campo obrigatório."
            page.update()
        if not Senha.value:
            Senha.error_text = "Campo obrigatório."
            page.update()
        else:
            nome = Usuario.value
            senha = Senha.value
            print(f"nome: {nome}\n senha: {senha}")
            page.clean()
            page.add(ft.Text(f"Olá, {nome}"))        

    def go_to_register(e):
        page.go("/register")

    Usuario = ft.TextField(
        label="Usuário",
        label_style=ft.TextStyle(color="black"), 
        width=300, 
        border_color="black", 
        color="black", 
        bgcolor="white"
    )
    
    Senha = ft.TextField(
        label="Senha",
        label_style=ft.TextStyle(color="black"),
        password=True,
        width=300,
        border_color="black",
        color="black",
        content_padding=ft.padding.symmetric(vertical=10, horizontal=10),  
        suffix=ft.IconButton(
            icon=ft.Icons.VISIBILITY, 
            icon_color="black",
            on_click=toggle_password,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=0)},  
                padding=ft.padding.all(0), 
            ),
        ),
        bgcolor="white",   
    )

    return ft.View(
    
        route="/",
        bgcolor="#f2dbc2", 
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src="psi.png", width=100, height=100),
                        Usuario,
                        Senha,
                        ft.Row(
                            [
                                ft.ElevatedButton("Login", on_click=login_action, color="white", width=150, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),  
                                    elevation=5, 
                                    overlay_color="rgba(255, 255, 255, 0.2)",
                                    bgcolor="#212121",
                                    color="#white")
                                ),
                                ft.ElevatedButton("Registrar", on_click=go_to_register, width=150, style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),  
                                    elevation=5, 
                                    overlay_color="rgba(255, 255, 255, 0.2)",
                                    bgcolor="#212121",
                                    color="white")
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  
                            spacing=10
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center, 
                expand=True  
            )
        ]
    )
