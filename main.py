import os
from rich.console import Console

ascii_art = """
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ██████╗     ███╗   ███╗██████╗ ██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ╚════██╗    ████╗ ████║██╔══██╗██║  ██║
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗       █████╔╝    ██╔████╔██║██████╔╝███████║
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝      ██╔═══╝     ██║╚██╔╝██║██╔═══╝ ╚════██║
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ███████╗    ██║ ╚═╝ ██║██║          ██║
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝    ╚══════╝    ╚═╝     ╚═╝╚═╝          ╚═╝
                                                                                                        
"""


class YouTubeDownloader:
    def __init__(self) -> None:
        self.url = None
        self.console = Console()

    def styled_input(self, prompt: str, style=None):
        if style:
            self.console.print(prompt, style=style, end="")
        else:
            self.console.print(prompt, end="")
        return input()

    def get_video_url(self) -> None:
        url = self.styled_input("Enter YouTube Video URL: ", style="bold blue")

        if url[:20] != "https://youtube.com" and url[:11] != "youtube.com":
            self.console.print("[bold red]Invalid URL. Please try again.[/bold red]")
            self.get_video_url()
        else:
            self.url = url

    def main_menu(self):
        while True:
            os.system("clear" if not os.name == "nt" else "cls")
            self.console.print(ascii_art, justify="center", style="#D3869B bold")
            self.console.print("[cyan]:: Download YouTube Videos ::[cyan]\n", justify="center", end="")
            self.console.print("1. Download Single Video      2. Download Multiple Videos     3. Exit",justify="center")
            choice = self.styled_input("Enter your choice: ", style="bold green")
            if choice == "1":
                self.download_single_video()
            elif choice == "2":
                self.download_multiple_videos()
            elif choice == "3":
                break
            else:
                self.console.print("[bold red]Invalid choice. Please try again.[/bold red]")

    def download_single_video(self):
        self.get_video_url()

    def download_multiple_videos(self):
        self.get_video_url()


if __name__ == "__main__":
    downloader = YouTubeDownloader()
    downloader.main_menu()
