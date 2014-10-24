Title: WirePrint: 3D Printed Previews For Fast Prototyping
Slug: wireprint-3d-printed-previews-for-fast-prototyping
Date: 2014-10-01 10:34:29
Summary: WirePrint is a low-fi fabrication technique that prints 3D models as wireframe previews. By extruding filament directly into 3D space instead of printing layer-wise, we achieve a speed-up of up to 10x compared to traditional 3D printing.

{% img left img-large shadowbox images/web_several-objects.jpg %}

## Abstract
Even though considered a rapid prototyping tool, 3D printing is so slow that a reasonably sized object requires printing overnight. This slows designers down to a single iteration per day. With WirePrint, we propose to instead print low-fidelity wireframe previews in the early stages of the design process. Wireframe previews are 3D prints in which surfaces have been replaced with a wireframe mesh. Since wireframe previews are to scale and represent the overall shape of the 3D object, they allow users to quickly verify key aspects of their 3D design, such as the ergonomic fit.

To maximize the speed-up, we instruct 3D printers to extrude filament not layer-by-layer, but directly in 3D-space, allowing them to create the edges of the wireframe model directly one stroke at a time. This allows us to achieve speed-ups of up to a factor of 10 compared to traditional layer-based printing. We demonstrate how to achieve wireframe previews on standard FDM 3D printers, such as the PrintrBot or the Kossel mini. Users only need to install the WirePrint software, making our approach applicable to many 3D printers already in use today. Finally, wireframe previews use only a fraction of material required for a regular print, making it even more affordable to iterate.

{% youtube Ea4V7kb2VsY %}

## Veröffentlichung
[Mueller, S.](http://stefaniemueller.org/), Im, S., Gurevich, S., Teibrich, A., Pfisterer, L., Guimbretière, F., and [Baudisch, P.](http://www.patrickbaudisch.com/): *WirePrint: Fast 3D Printed Previews*. 
In Proceedings of UIST’14 (Full Paper, to appear). [doi: 10.1145/2642918.2647359](http://dx.doi.org/10.1145/2642918.2647359)

## Pressemitteilung
Hasso Plattner Institut Potsdam: WirePrint - 3D Printed Previews for Fast Prototyping. [https://www.hpi.uni-potsdam.de/baudisch/projects/wireprint.html]()

## Presseberichte
* 3ders: Introducing WirePrint: 3D printed wireframe previews speeds up prototyping by 10x. [http://www.3ders.org/articles/20140917-wireprint-3d-printed-wireframe-previews-speeds-up-prototyping.html]()
* Hack A Day: WirePrint is a Physical ‘Print Preview’ for 3D Printers. [http://hackaday.com/2014/09/27/wireprint-is-a-physical-print-preview-for-3d-printers/]()
* gadgetify: WirePrint for Fast Prototyping. [http://www.gadgetify.com/wireprint/]()