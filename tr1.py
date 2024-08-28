import flet as ft

def main(page: ft.Page):

    # Função para adicionar uma nova tarefa
    def adicionar_tarefa(e):
        if txt_tarefa.value and txt_data.value:
            tarefas.controls.append(
                ft.Row(
                    controls=[
                        ft.Checkbox(),
                        ft.Text(f"{txt_tarefa.value} - Data limite: {txt_data.value}")
                    ]
                )
            )
            txt_tarefa.value = ""
            txt_data.value = ""
            page.update()
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Por favor, preencha todos os campos!"))
            page.dialog.open = True
            page.update()

    # Função para excluir uma tarefa selecionada
    def excluir_tarefa(e):
        tarefas.controls = [tarefa for tarefa in tarefas.controls if not tarefa.controls[0].value]
        page.update()

    # Configuração da interface
    txt_tarefa = ft.TextField(label="Tarefa", width=300)
    txt_data = ft.TextField(label="Data limite (dd/mm/aaaa)", width=200)
    
    tarefas = ft.Column()

    page.add(
        ft.Column(
            [
                txt_tarefa,
                txt_data,
                ft.Row(
                    [
                        ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa),
                        ft.ElevatedButton("Excluir Tarefa Concluída", on_click=excluir_tarefa),
                    ]
                ),
                tarefas,
            ]
        )
    )

ft.app(target=main)
