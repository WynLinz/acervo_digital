import threading
import subprocess
import customtkinter as ctk
from tkinter import messagebox
import os


class ScieloGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Scielo Scraper')
        self.geometry('900x700')
        self.proc = None
        self._build()

    def _build(self):
        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('blue')

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill='both', expand=True, padx=16, pady=16)

        self.btn_frame = ctk.CTkFrame(self.frame)
        self.btn_frame.pack(fill='x', pady=(0,8))

        self.start_btn = ctk.CTkButton(self.btn_frame, text='Iniciar', command=self.on_start)
        self.start_btn.pack(side='left')

        self.clear_btn = ctk.CTkButton(self.btn_frame, text='Limpar', command=self.on_clear)
        self.clear_btn.pack(side='left', padx=(10,0))

        self.status = ctk.CTkLabel(self.frame, text='Pronto', fg_color=None)
        self.status.pack(anchor='w', pady=(8,0))

        self.textbox = ctk.CTkTextbox(self.frame, width=850, height=400)
        self.textbox.pack(fill='both', expand=True, pady=(12,0))
        self.textbox.configure(state='disabled')

        # Caixa de prompt para enviar comandos ao processo
        self.prompt_frame = ctk.CTkFrame(self.frame)
        self.prompt_frame.pack(fill='x', pady=(16,0))
        self.prompt_label = ctk.CTkLabel(self.prompt_frame, text='Prompt:')
        self.prompt_label.pack(side='left')
        self.prompt_entry = ctk.CTkEntry(self.prompt_frame, width=600)
        self.prompt_entry.pack(side='left', padx=(8,0), fill='x', expand=True)
        self.prompt_entry.bind('<Return>', self.on_send_prompt)
        self.send_btn = ctk.CTkButton(self.prompt_frame, text='Enviar', command=self.on_send_prompt)
        self.send_btn.pack(side='left', padx=(8,0))

    def on_clear(self):
        self.textbox.configure(state='normal')
        self.textbox.delete('1.0', 'end')
        self.textbox.configure(state='disabled')
        self.status.configure(text='Pronto')

    def on_start(self):
        if self.proc and self.proc.poll() is None:
            messagebox.showinfo('Info', 'O processo já está em execução.')
            return
        self.start_btn.configure(state='disabled')
        self.status.configure(text='Executando... (veja o log abaixo)')
        self.on_clear()
        thread = threading.Thread(target=self._run_scraper, daemon=True)
        thread.start()

    def _run_scraper(self):
        script_path = os.path.join(os.path.dirname(__file__), 'scielo_v2.py')
        cmd = ['python', script_path]
        try:
            self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, text=True, bufsize=1)
        except Exception as e:
            self._append_text(f'Erro ao iniciar o scraper: {e}\n')
            self._on_scraper_done()
            return

        for line in iter(self.proc.stdout.readline, ''):
            if not line:
                break
            self._append_text(line)
        self.proc.stdout.close()
        self.proc.wait()
        self._on_scraper_done()

    def _append_text(self, text):
        def cb():
            self.textbox.configure(state='normal')
            self.textbox.insert('end', text)
            self.textbox.see('end')
            self.textbox.configure(state='disabled')
        self.after(0, cb)

    def _on_scraper_done(self):
        def cb():
            self.start_btn.configure(state='normal')
            self.status.configure(text='Execução finalizada')
            self.proc = None
        self.after(0, cb)

    def on_send_prompt(self, event=None):
        text = self.prompt_entry.get().strip()
        if not text:
            return
        if not self.proc or self.proc.poll() is not None:
            messagebox.showwarning('Aviso', 'O processo não está em execução.')
            return
        try:
            self.proc.stdin.write(text + '\n')
            self.proc.stdin.flush()
            self._append_text(f'> {text}\n')
            self.prompt_entry.delete(0, 'end')
        except Exception as e:
            messagebox.showerror('Erro', f'Falha ao enviar comando: {e}')

def main():
    app = ScieloGUI()
    app.mainloop()

if __name__ == '__main__':
    main()
