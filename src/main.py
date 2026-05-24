import flet as ft

TITLE = "StudyFold"
DATA_FILE = "data.json"



PRIMARY   = "#6C63FF"   
BG        = "#EBEDF0"
SURFACE = "#FFFFFF"
ON_BG   = "#1A1A2E"

class Tile(ft.ExpansionPanel):
    def __init__(self, question, answer):
        super().__init__(
            header=ft.ListTile(title=ft.Text(question)),
            content=ft.Container(
                padding=10,
                content=ft.Text(answer)
            ),
            can_tap_header=True
        )

class CardView(ft.Column):
    def __init__(self):
        super().__init__()


class StudyView(ft.Column):
    def __init__(self):
        super().__init__()

class Header(ft.Row):
    def __init__(self, title, onclick):
        super().__init__()
        self.controls = [
            ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
            ft.IconButton(icon=ft.Icons.MENU_ROUNDED, on_click=onclick)
        ]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

class SideBar(ft.Container):
    def __init__(self):
        super().__init__()
        self.width   = 0
        self.bottom  = 0
        self.top     = 0
        self.bgcolor = SURFACE
        self.left    = -210
        self.border_radius = 10
        self.padding = ft.Padding.all(15)
        self.animate_position = ft.Animation(150, ft.AnimationCurve.EASE_IN_OUT)
        self.shadow  = ft.BoxShadow(blur_radius=12, color="#22000000")
        self.content = ft.Column([
            ft.Text("StudyFold", text_align = ft.TextAlign.CENTER, size=16, weight=ft.FontWeight.BOLD,
                    color=ON_BG),
            ft.Divider(),
            ft.TextButton("Settings", icon=ft.Icons.SETTINGS_ROUNDED),
            ft.TextButton("About",    icon=ft.Icons.INFO_ROUNDED),
        ], spacing=10)

    def toggle(self):
        self.width = 210 if self.width == 0 else 0
        self.left = 0 if self.left == -210 else -210
        self.update()

class AddCardSheet(ft.BottomSheet):
    def __init__(self):
        self.question = ft.TextField(
            label="Question",
            multiline=True,
            min_lines=2,
            max_lines=5
        )
        self.answer = ft.TextField(
            label="Answer",
            multiline=True,
            min_lines=2,
            max_lines=5
        )
        self.course = ft.TextField(label="Course")
        self.topic = ft.TextField(label="Topic")

        content = ft.Container(
            padding=ft.Padding.only(left=35, right=20, top=16, bottom=24),
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                tight=True,
                spacing=15,
                controls=[
                    ft.Text(
                        "Add Your Q and A",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),

                    self.question,
                    self.answer,
                    self.course,
                    self.topic,

                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton("Cancel"),
                            ft.TextButton("Save")
                        ]
                    )
                ]
            )
        )

        super().__init__(
            content=content,
            open=False,
            show_drag_handle=True,
            scrollable=True,

        )
def main(page: ft.Page):
    page.title = TITLE
    page.window.width = 400
    page.window.height = 700
    page.bgcolor = BG

    def open_side_bar(e):
        side_bar.toggle()
        page.update()

    def change_tab(e):
        index = e.control.selected_index

        if index == 1:
            sheet.open = True

        page.update()

    content = ft.Column(expand=True)

    header = Header(TITLE, open_side_bar)

    side_bar = SideBar()
    sheet = AddCardSheet()

    bottom_bar = ft.NavigationBar(
        on_change=change_tab,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.SCHOOL_ROUNDED, label="Study"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ADD, label="ADD"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.STYLE, label="Cards"
            )
        ],
    )
    
    page.overlay.append(sheet)
    page.navigation_bar = bottom_bar
    page.add(
        ft.Container(
            expand=True,
            content=ft.SafeArea(
                content=ft.Stack([
                    ft.Column([
                        header,
                        ft.Divider(),
                        content
                    ], expand=True),
                    side_bar
                ], expand=True)
            )
        )
    )

    
ft.run(main)
