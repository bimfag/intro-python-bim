from OCC.Display.WebGl.jupyter_renderer import JupyterRenderer as Renderer

class ifc_viewer(Renderer):
    def __init__(self):
        Renderer.__init__(self)
        self.n = 0
        self.products = []

    @staticmethod
    def subshapes(shp):
        import OCC.TopoDS
        it = OCC.TopoDS.TopoDS_Iterator(shp)
        while it.More():
            yield it.Value()
            it.Next()

    def DisplayShape(self, product, shp, color):
        for shp, sty in zip(self.subshapes(shp), color):
            Renderer.DisplayShape(self, shp, shape_color=sty[0:3], show=False, render_edges=True)
            self.products.append(product)

    def onclick(self, item):
        self.html.value = "Selected %r" % self.products[int(item.name)]

