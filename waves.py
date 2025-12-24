import pyglet


class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(resizable=True, caption="Waves")
        self.set_minimum_size(320, 200)

        self.fps_display = pyglet.window.FPSDisplay(self)

        self.label = pyglet.text.Label(
            "Hello, world",
            font_name="Times New Roman",
            font_size=36,
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )

    def on_draw(self):
        self.clear()
        self.label.draw()
        self.fps_display.draw()

    def on_resize(self, width, height):
        print(f"The window was resized to {width},{height}")
        self.label.x = self.width // 2
        self.label.y = self.height // 2


if __name__ == "__main__":
    window = MainWindow()
    pyglet.app.run()
