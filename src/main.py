import flet as ft


def main(page: ft.Page) -> None:
    counter = ft.Text(value="0", size=50)
    counter.data = 0  # Explicitly set the type of data to int

    def increment_click(e: ft.ControlEvent) -> None:
        counter.data += 1
        counter.value = str(object=counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            content=ft.Container(
                content=counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(target=main)
