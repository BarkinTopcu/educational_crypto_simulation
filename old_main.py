import gradio as gr
from exchange_simulator import ExchangeSimulator
import pandas as pd
from CSS_Styles import CSS_Styles
import matplotlib.pyplot as plt

class AutoCrypto:
    def __init__(self):
        self.css = CSS_Styles().get_styles()
        self.page = None
        self.data_crypto = {}

#################################
#           INTERFACE           #
#################################
    def create_interface(self):
        with gr.Blocks(css=self.css) as interface:
            gr.Markdown("# Crypto Bot Simulation - Educational Purpose Only")
            gr.Markdown("""
            ### ⚠️ Disclaimer / Sorumluluk Reddi

            **English:**  
            This application is developed for educational purpose only. It does **not** provide financial or investment advice. All investment decisions made based on this application are at the sole discretion and risk of the user. The developer assumes **no responsibility** for any financial loss or damage resulting from the use of this tool.

            **Türkçe:**  
            Bu uygulama yalnızca eğitim amaçlı geliştirilmiştir. **Yatırım tavsiyesi niteliği taşımaz.** Uygulama aracılığıyla yapılan tüm yatırım kararları tamamen kullanıcının kendi inisiyatifinde ve sorumluluğundadır. Uygulamanın geliştiricisi, kullanım sonucu oluşabilecek hiçbir maddi zarardan **sorumlu değildir.**
            """)

            #Top Menu Bar
            with gr.Row(elem_classes="menu-row",equal_height=False):
                page1_button = gr.Button("Simulation Crpyto Buy", elem_classes="small-button-red")
                page2_button = gr.Button("Portfolio User", elem_classes="small-button-yellow")
                page3_button = gr.Button("Analysis",elem_classes="small-button-green")
            
            page1 = self.page1_layout()
            page2 = self.page1_layout()
            page3 = self.page1_layout()
            pages = [page1,page2,page3]
            buttons = [page1_button, page2_button, page3_button]
            for idx, button in enumerate(buttons):
                button.click(
                    lambda i=idx: [gr.update(visible=j == i) for j in range(3)],
                    inputs=[], outputs=pages
                )

        return interface
    
    def page1_layout(self):
        with gr.Column(visible=False) as page1:
            gr.Markdown("# Simulation Data")
            crypto_dropdown = None
            period_dropdown = None
            crypto_dropdown = gr.Dropdown(label="Crypto", choices=[], interactive=True)
            period_dropdown = gr.Dropdown(label="Period", choices=[], interactive=True)
            with gr.Row():
                data_file_input = gr.File(label="Upload File",elem_id="file_input")
                modify_data_crypto_name = gr.Textbox(label="Crpyto Name", placeholder="BTC")
                modify_data_crypto_period = gr.Textbox(label="Data Period", placeholder="30 mn")
                modify_data_crypto_radio = gr.Radio(
                    choices=["Add", "Remove"],
                    label="Choose an Option"
                )
                modify_data_crypto_button = gr.Button("Modify")
                modify_data_crypto_button.click(
                    self.data_crypto_modify,
                    inputs=[data_file_input,modify_data_crypto_name,modify_data_crypto_period,modify_data_crypto_radio],
                    outputs=[crypto_dropdown]
                )



            plot_button = gr.Button("Plot Data")
            output_plot = gr.Plot()

            def update_periods(crypto_name):
                if crypto_name in self.data_crypto:
                    return gr.update(choices=list(self.data_crypto[crypto_name].keys()))
                return gr.update(choices=[])

            crypto_dropdown.change(fn=update_periods, inputs=crypto_dropdown, outputs=period_dropdown)

            plot_button.click(
                fn=self.plot_crypto_data,
                inputs=[crypto_dropdown, period_dropdown],
                outputs=output_plot
            )


        return page1

    def plot_crypto_data(self,crypto_name, period):

        if crypto_name not in self.data_crypto:
            raise ValueError("Crypto bulunamadı.")
        if period not in self.data_crypto[crypto_name]:
            raise ValueError("Period bulunamadı.")

        data = self.data_crypto[crypto_name][period]["data"]
        if len(data) > 5000:
            data = data.sample(5000).sort_index()

        plt.figure(figsize=(8, 4))
        plt.plot(data.iloc[:, 0], data.iloc[:, 1])
        plt.xlabel(data.columns[0])
        plt.ylabel(data.columns[1])
        plt.title(f"{crypto_name} - {period}")
        plt.grid(True)

        # Gradio'da görünmesi için return gerekiyor
        return plt.gcf()  # Figure objesini döndür
#################################
#           FUNCTIONS           #
#################################

    def data_crypto_modify(self, data_file_input: str, modify_data_crypto_name : str,modify_data_crypto_period : str ,modify_data_crypto_radio: str):
        if modify_data_crypto_radio == "Add":
            data = pd.read_csv(data_file_input)
            if modify_data_crypto_name not in self.data_crypto:
                self.data_crypto[modify_data_crypto_name] = {}
            self.data_crypto[modify_data_crypto_name][modify_data_crypto_period] = {
                "file": data_file_input,
                "data": data
            }
            print("Data ekleme işlemi Başarılı")
        elif modify_data_crypto_radio == "Remove":
            if (
                modify_data_crypto_name in self.data_crypto and
                modify_data_crypto_period in self.data_crypto[modify_data_crypto_name]
            ):
                del self.data_crypto[modify_data_crypto_name][modify_data_crypto_period]

                if not self.data_crypto[modify_data_crypto_name]:
                    del self.data_crypto[modify_data_crypto_name]
                print("Data silme İşlemi Başarılı")
            else:
                print("Data silme işlemi Başarısız")
        else:
            raise ValueError("Please select an option: 'Add' or 'Remove'.")
        
        return gr.update(choices=list(self.data_crypto.keys()))

if __name__ == "__main__":
    app = AutoCrypto()
    interface = app.create_interface()
    interface.launch(share=False)
