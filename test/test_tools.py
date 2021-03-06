import numpy
import pytest

import colorio


@pytest.mark.parametrize(
    "colorspace, cut_000",
    [
        (colorio.CIELAB(), False),
        # (colorio.XYY(), True),
        (colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5), False),
    ],
)
def test_srgb_gamut(colorspace, cut_000, n=10):
    colorspace.save_srgb_gamut("srgb.vtu", n=n, cut_000=cut_000)
    return


@pytest.mark.parametrize(
    "colorspace",
    [
        colorio.CIELAB(),
        colorio.XYY(),
        colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5),
    ],
)
def test_cone_gamut(colorspace, n=10):
    observer = colorio.observers.cie_1931_2()
    colorspace.save_cone_gamut("cone.vtu", observer, max_Y=1)
    return


@pytest.mark.parametrize(
    "colorspace", [colorio.CIELAB(), colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5)]
)
def test_hdr_gamut(colorspace, n=10):
    colorspace.save_hdr_gamut("hdr.vtu", n=n)
    return


@pytest.mark.parametrize(
    "colorspace,cut_000",
    [
        # (colorio.CIELAB(), False),
        # (colorio.XYY(), True),
        (colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5), False)
    ],
)
def test_visible_gamut(colorspace, cut_000):
    illuminant = colorio.illuminants.d65()
    observer = colorio.observers.cie_1931_2()
    colorspace.save_visible_gamut(observer, illuminant, "visible.vtu", cut_000=cut_000)
    return


def test_flat_gamut(xy_to_2d=lambda xy: xy):
    colorio.show_flat_gamut()
    return


@pytest.mark.parametrize(
    "a", [numpy.random.rand(3), numpy.random.rand(3, 7), numpy.random.rand(3, 4, 5)]
)
def test_conversion_variants(a):
    b = a + 1.0e-3 * numpy.random.rand(*a.shape)
    diff = colorio.delta(a, b)
    assert diff.shape == a.shape[1:]
    return


@pytest.mark.parametrize(
    "colorspace", [colorio.CIELAB(), colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5)]
)
def test_ebner_fairchild(colorspace):
    colorspace.show_ebner_fairchild()
    return


@pytest.mark.parametrize(
    "colorspace", [colorio.CIELAB(), colorio.CAM02("UCS", 0.69, 20, 64 / numpy.pi / 5)]
)
def test_hung_berns(colorspace):
    colorspace.show_hung_berns()
    return


@pytest.mark.parametrize("colorspace", [colorio.CIELAB()])
def test_xiao(colorspace):
    colorspace.show_xiao()
    return


@pytest.mark.parametrize("colorspace", [colorio.CIELAB()])
def test_munsell(colorspace):
    colorspace.show_munsell(V=5)
    return


def test_macadam():
    def xy_to_2d(xy):
        x, y = xy
        return numpy.array([4 * x, 9 * y]) / (-2 * x + 12 * y + 3)

    # def xy_to_2d(xy):
    #     return xy

    colorio.show_macadam(
        ellipse_scaling=10,
        xy_to_2d=xy_to_2d,
        # plot_standard_deviations=True,
        # axes_labels=['u\'', 'v\'']
    )
    return


def test_luo_rigg():
    colorio.show_luo_rigg(ellipse_scaling=1.5)
    return


def test_show_straights(cs=colorio.CIELAB()):
    colorio.show_straights(cs)
    return


def test_xy_gamut_mesh():
    points, cells = colorio.xy_gamut_mesh(0.05)

    # import meshio
    # meshio.write_points_cells("test.vtu", points, {"triangle": cells})
    # exit(1)
    return


if __name__ == "__main__":
    # test_luo_rigg()
    # test_xy_gamut_mesh()
    # test_macadam()
    # colorspace_ = colorio.SrgbLinear()
    # colorspace_ = colorio.Hdr()
    # colorspace_ = colorio.XYZ()
    colorspace_ = colorio.XYY()
    # colorspace_ = colorio.IPT()
    # colorspace_ = colorio.JzAzBz()
    # colorspace_ = colorio.CIELUV()
    # colorspace_ = colorio.CIELAB()
    # colorspace_ = colorio.CAM02('UCS', 0.69, 20, 64/numpy.pi/5)
    # colorspace_ = colorio.CAM16UCS(0.69, 20, 64 / numpy.pi / 5)
    # test_hdr_gamut(colorspace_, n=10)
    # test_visible_gamut(colorspace_, cut_000=False)
    # test_srgb_gamut(colorspace_, cut_000=False)
    # test_ebner_fairchild(colorspace_)
    test_hung_berns(colorspace_)
    # test_xiao(colorspace_)
    # test_show_straights(colorspace_)
    # test_munsell(colorspace_)
    # test_cone_gamut(colorio.XYY())
    # test_cone_gamut(colorio.XYZ())
    # test_cone_gamut(colorio.CIELAB())
