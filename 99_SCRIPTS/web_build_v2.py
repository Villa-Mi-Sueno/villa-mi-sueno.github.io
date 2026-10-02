"""VMS · Welcome Pack web · v2  (opción C, elegida por Miguel 2026-10-01)
Estructura y componentes del Figma "VMS" (app de 4 pestañas, fondo crema, tarjetas) +
familias de color de FAMILIAS.md como acento + tipografía de BRAND.md (Philosopher Bold + Montserrat).
Uso:  python3 99_SCRIPTS/web_build_v2.py   ->   08_WELCOME_WEB/sitio_v2/vms/index.html
No toca sitio/ (v1).  Fotos: deja JPG en 08_WELCOME_WEB/_fuente/fotos/<slot>.jpg y vuelve a ejecutar.
Slots: portada · anfitriones · casa · piscina · explora
"""
import os, re, json, shutil, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(R, "08_WELCOME_WEB"); OUT = os.path.join(W, "sitio_v2")
FOT = os.path.join(W, "_fuente", "fotos")
ICO = os.path.join(R, "01_ICONOS", "SVG_SIN_FONDO")
BBOX = json.load(open(os.path.join(ICO, "_bbox.json")))
e = html.escape

# ---------------- familias (FAMILIAS.md) ----------------
FAM = {"bienvenida": ("#F6AECE", False), "llegada": ("#B5DDC1", False), "casa": ("#99234E", True),
       "piscina": ("#141F3A", True), "debes": ("#EDA23E", False), "wifi": ("#272525", True),
       "comparte": ("#CCCACA", False), "jarabacoa": ("#505D3C", True), "emergencias": ("#9E1B14", True)}
def fs(f):
    acc, dark = FAM[f]
    ink = acc if dark else "#141F3A"          # acento usado como texto/icono (claros -> azul, regla BRAND §3)
    on = "#F2EDE4" if dark else "#141F3A"     # contenido sobre el color pleno
    chip = f"color-mix(in srgb,{acc} 14%,#FFFDF8)" if dark else acc
    tint = f"color-mix(in srgb,{acc} 8%,#FFFDF8)" if dark else f"color-mix(in srgb,{acc} 30%,#FFFDF8)"
    return f'style="--acc:{acc};--ink:{ink};--on:{on};--chip:{chip};--tint:{tint}"'

# ---------------- iconos UI (línea, 24px) ----------------
I = {
 "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "tel": '<path d="M5 3h3l2 5-2.5 1.5a11 11 0 0 0 5 5L14 12l5 2v3a2 2 0 0 1-2 2A15 15 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
 "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".8" fill="currentColor"/>',
 "web": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "trip": '<circle cx="7.5" cy="13.5" r="3.5"/><circle cx="16.5" cy="13.5" r="3.5"/><path d="M2.5 9h19M10 9.5l2 2.5 2-2.5"/>',
 "ruta": '<path d="M3 19l5.5-13 4 8 3-5L21 19"/>',
 "wifi": '<path d="M2 8.5a15 15 0 0 1 20 0M5 12a10 10 0 0 1 14 0M8.5 15.5a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1" fill="currentColor"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "chat": '<path d="M4 20l1.5-4A8 8 0 1 1 9 19z"/>',
 "home": '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3M14 9l2 2"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "clip": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M9 12.5l2 2 4-4"/>',
 "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "in": '<path d="M10 17l5-5-5-5M15 12H3M15 4h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-4"/>',
 "out": '<path d="M14 17l5-5-5-5M19 12H8M10 20H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h5"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>',
 "siren": '<path d="M7 18v-6a5 5 0 0 1 10 0v6M5 18h14v3H5zM12 2v2M4 6l1.5 1.5M20 6l-1.5 1.5"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M12 9v6M9 12h6"/>',
 "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "heart": '<path d="M12 20s-8-4.8-8-10.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 8 2.5C20 15.2 12 20 12 20z"/>',
 "fork": '<path d="M7 3v8a2 2 0 0 0 4 0V3M9 11v10M17 3c-2 0-3 3-3 7h3v11"/>',
 "mountain": '<path d="M3 20l6.5-11 4 6 2.5-4L21 20z"/>',
 "trees": '<path d="M8 3l5 8H3zM8 9l5 7H3zM8 16v5M17 7l4 7h-8zM17 14v7"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "bag": '<path d="M5 8h14l-1 13H6zM9 8V6a3 3 0 0 1 6 0v2"/>',
 "book": '<path d="M4 4h11a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z"/><path d="M8 8h6M8 12h6"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
 "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
 "towel": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M5 8h14M9 13h6"/>',
 "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 21h4"/>',
 "sofa": '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3M3 12a2 2 0 0 1 4 0v2h10v-2a2 2 0 0 1 4 0v6H3zM5 18v2M19 18v2"/>',
 "table": '<path d="M3 9h18M5 9l-1 11M19 9l1 11M12 9v11"/>',
 "decor": '<rect x="4" y="4" width="16" height="12" rx="1"/><path d="M8 20l4-4 4 4"/>',
 "star": '<path d="M12 3l2.8 5.8 6.2.9-4.5 4.4 1 6.2-5.5-2.9-5.5 2.9 1-6.2L3 9.7l6.2-.9z"/>',
 "bed": '<path d="M3 18V7M3 13h18v5M21 18v-3a3 3 0 0 0-3-3h-7v1M7 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>',
 "snow": '<path d="M12 2v20M4 6l16 12M20 6L4 18"/>',
 "bath": '<path d="M3 12h18v3a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5zM6 12V5a2 2 0 0 1 4 0"/>',
 "waves": '<path d="M2 9c2.5-2 4.5-2 7 0s4.5 2 7 0 4.5-2 6 0M2 15c2.5-2 4.5-2 7 0s4.5 2 7 0 4.5-2 6 0"/>',
 "sparkles": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
 "flame": '<path d="M12 21a6 6 0 0 0 6-6c0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-2 2-3 5-3 8a6 6 0 0 0 6 6z"/>',
 "grill": '<path d="M4 9h16a8 8 0 0 1-16 0zM8 17l-2 4M16 17l2 4M9 5c0-1 1-1 1-2M14 5c0-1 1-1 1-2"/>',
 "pot": '<path d="M4 10h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4zM2 10h2M20 10h2M9 6h6"/>',
 "pizza": '<path d="M12 21L3 6a14 14 0 0 1 18 0z"/><circle cx="10" cy="10" r="1"/><circle cx="14" cy="13" r="1"/>',
 "circle": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2"/>',
 "dice": '<rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="9" cy="9" r="1" fill="currentColor"/><circle cx="15" cy="15" r="1" fill="currentColor"/><circle cx="15" cy="9" r="1" fill="currentColor"/><circle cx="9" cy="15" r="1" fill="currentColor"/>',
 "baby": '<circle cx="12" cy="8" r="4"/><path d="M6 21a6 6 0 0 1 12 0M10 8h.01M14 8h.01"/>',
 "car": '<path d="M4 16V12l2-5h12l2 5v4zM3 16h18v3H3zM7 19v2M17 19v2"/>',
 "desk": '<path d="M3 8h18M5 8v12M19 8v12M5 13h7"/>',
}
def ic(k, cls="i"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[k]}</svg>')
def bico(code):  # icono de marca aprobado (01_ICONOS)
    m = [x for x in os.listdir(ICO) if x.startswith(code + "_") and x.endswith(".svg") and not x.endswith("_alt.svg")]
    if not m: raise SystemExit(f"Icono no encontrado: {code!r}")
    f = m[0]
    return f'<img class="bi" src="../assets/icons/{f}" alt="" loading="lazy">'
def chip(icon, no=False, size=""):
    inner = bico(icon) if icon.startswith("ICO") else ic(icon)
    return f'<span class="chip {size}{" no" if no else ""}">{inner}</span>'

# ---------------- piezas del Figma ----------------
def eyebrow(t): return f'<div class="eb"><i></i><span>{e(t)}</span></div>'
def header(fam, eb, title, intro): return f'<header class="hd" {fs(fam)}>{eyebrow(eb)}<h1>{title}</h1><p>{e(intro)}</p></header>'
def h2(t, det="", id_=""): return f'<div class="h2"{f" id={chr(34)}{id_}{chr(34)}" if id_ else ""}><h2>{e(t)}</h2>{f"<span>{e(det)}</span>" if det else ""}</div>'
def row(text, icon="check", no=False): return f'<li class="row">{chip(icon, no)}<span>{text}</span></li>'
def rows(items): return '<ul class="rows">' + "".join(row(*x) if isinstance(x, tuple) else row(x) for x in items) + "</ul>"
def group(fam, title, icon, items, dato="", id_="", extra=""):
    d = f'<span class="dato">{e(dato)}</span>' if dato else ""
    return (f'<article class="card grp" {fs(fam)}{f" id={chr(34)}{id_}{chr(34)}" if id_ else ""}><div class="gh">'
            f'<div class="tema">{chip(icon, size="m")}<h3>{e(title)}</h3></div>{d}</div><hr>{rows(items)}{extra}</article>')
def info(fam, icon, label, value, detail="", acts="", tint=False):
    return (f'<article class="card info{" tint" if tint else ""}" {fs(fam)}>{chip(icon, size="l")}<div>'
            f'<span class="lb">{e(label)}</span><b>{value}</b>{f"<p>{detail}</p>" if detail else ""}{acts}</div></article>')
def nota(t): return f'<p class="nota"><b>Pendiente:</b> {t}</p>'

def foto(slot, cls, inner, desc):
    src = os.path.join(FOT, slot + ".jpg")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(OUT, "assets", "fotos", slot + ".jpg"))
        return f'<div class="{cls}" style="background-image:url(../assets/fotos/{slot}.jpg)"><div class="vel"></div>{inner}</div>'
    return f'<div class="{cls} ph" data-ph="Foto pendiente · {e(desc)}"><div class="vel"></div>{inner}</div>'

# ---------------- enlaces ----------------
def tel(n):
    d = "".join(c for c in n if c.isdigit())
    return "tel:+" + (d if len(d) == 11 else "1" + d)
M = lambda k: "https://maps.app.goo.gl/" + k
IG = lambda h: "https://www.instagram.com/" + h + "/"
ACT = {"tel": ("tel", "Llamar"), "maps": ("pin", "Cómo llegar"), "ig": ("ig", "Instagram"), "web": ("web", "Web"),
       "trip": ("trip", "TripAdvisor"), "ruta": ("ruta", "Rutas en Wikiloc")}
def acts(name, **L):
    out = ""
    for k in ("tel", "maps", "ig", "web", "trip", "ruta"):
        if k in L and L[k]:
            u = tel(L[k]) if k == "tel" else L[k]
            icon, lab = ACT[k]
            out += f'<a class="ab" href="{e(u)}"{"" if k == "tel" else " target=_blank rel=noopener"} aria-label="{lab} · {e(name)}" title="{lab}">{ic(icon)}</a>'
    return f'<div class="acts">{out}</div>'
def place(name, sub="", star=False, **L):
    return (f'<div class="pl{" star" if star else ""}"><div class="pn"><b>{e(name)}</b>{f"<small>{e(sub)}</small>" if sub else ""}</div>'
            f'{acts(name, **L)}</div>')
def places(fam, lst, id_="", note=""):
    return f'<div class="card list" {fs(fam)}{f" id={chr(34)}{id_}{chr(34)}" if id_ else ""}>' + "".join(place(**p) for p in lst) + "</div>" + (nota(note) if note else "")

# ---------------- datos (PDF VMS WELCOME PACK-2026 + _fuente/sitios.json) ----------------
TRIP_PARA = "https://www.tripadvisor.es/Attractions-g675009-Activities-c61-t192-Jarabacoa_La_Vega_Province_Dominican_Republic.html"
TRIP_RAFT = "https://www.tripadvisor.es/Attractions-g675009-Activities-c61-t193-Jarabacoa_La_Vega_Province_Dominican_Republic.html"
NATURALEZA = [
 dict(name="Río Camú", sub="Balneario a menos de 3 km, dentro de Mata de Plátano", star=True, maps=M("BJHcjE3TcBzNr8hk8")),
 dict(name="Salto Jimenoa", maps=M("y8ChwUkAP5zbywGp6"), trip="https://www.tripadvisor.es/Attraction_Review-g675009-d23606309-Reviews-Salto_De_Jimenoa_Uno-Jarabacoa_La_Vega_Province_Dominican_Republic.html"),
 dict(name="Salto Baiguate", maps=M("R9L8x3Vd9mevCknK7"), trip="https://www.tripadvisor.es/Attraction_Review-g675009-d3440196-Reviews-Baiguate_Salto_Waterfall-Jarabacoa_La_Vega_Province_Dominican_Republic.html"),
 dict(name="La Confluencia", maps=M("FvN7xcshWWdAwLG67"), trip="https://www.tripadvisor.es/Attraction_Review-g675009-d4978569-Reviews-La_Confluencia-Jarabacoa_La_Vega_Province_Dominican_Republic.html")]
AVENTURA = [
 ("Parapente", "mountain", TRIP_PARA, [
   dict(name="Hawk Paragliding", tel="8098787366", maps=M("DU8sCg46inxDxNFk8"), web="https://www.hawkparagliding.com/"),
   dict(name="Ecoparapente RD", tel="8092723084", maps=M("5EFexM74fymmHKFK9"), ig=IG("ecoparapenterd")),
   dict(name="FT Parapente", tel="8098483479", maps=M("zCPrmCWbQfyxym516"), ig=IG("ftparapente"))]),
 ("Buggys y four wheels", "car", "", [
   dict(name="Wheel Coyote", tel="8098200570", ig=IG("wheelcoyote")),
   dict(name="Jarabacoa 4 Wheel Rental", tel="8096664211", ig=IG("jarabacoa_4wheel_rental"))]),
 ("Rafting y tubing", "waves", TRIP_RAFT, [
   dict(name="Rancho Baiguate", tel="18294518851", maps=M("DU8sCg46inxDxNFk8"), web="https://www.ranchobaiguate.com/"),
   dict(name="Jaraventura", tel="8498856574", maps=M("9ewVSdjdasCTgTH47"), ig=IG("jaraventura")),
   dict(name="Mt. Xplor", maps=M("PMNZ1E22J1pe646t5"), ig=IG("mt.xplor"))]),
 ("Senderismo y mountain bike", "ruta", "", [
   dict(name="Rutas de senderismo", sub="Las mejores rutas en Jarabacoa", ruta="https://es.wikiloc.com/rutas/senderismo/republica-dominicana/la-vega/jarabacoa"),
   dict(name="Rutas de mountain bike", sub="En Jarabacoa", ruta="https://es.wikiloc.com/rutas/mountain-bike/republica-dominicana/la-vega/jarabacoa")])]
TRANQUILOS = [
 dict(name="Paseo a caballo", maps=M("FvN7xcshWWdAwLG67")),
 dict(name="City Tour", maps=M("sKcep15W1yWRuoqj7")),
 dict(name="Rancho Miel RD", sub="Petting zoo · animales de granja", tel="8295693449", maps=M("RjcRk4AmL81VXtn76"), ig=IG("ranchomielrd")),
 dict(name="Mariposario", sub="Solo por temporadas: verifica disponibilidad", tel="18294518851", maps=M("DU8sCg46inxDxNFk8"), web="https://www.ranchobaiguate.com/"),
 dict(name="Helados Ivon", maps=M("H2WgjPjrWJSe22o78"), ig=IG("helados_ivon_official")),
 dict(name="Rancho Bariloche", sub="Orquidiario y suculentas", maps=M("3gjE7x4FDYiJFty29"), ig=IG("ranchobariloche")),
 dict(name="Flores de Jarabacoa", sub="Visitas guiadas por sus sembradíos", maps=M("GcGQrBfqVXfHTa1W6"), ig="https://www.instagram.com/p/CgeeCcurFdm/")]
COMER = [
 dict(name="Herbes Farm to Table", tel="+18294237589", maps=M("xbqjMgb2WDhvEJfC9"), ig="https://www.instagram.com/explore/locations/122616990942228/herbes-farm-to-table/"),
 dict(name="Cayena by María Marte", maps=M("Zw3tSGsiEmhkSAYp6"), ig=IG("cayenabymariamarte")),
 dict(name="Ribera Country Club", tel="+18093654664", maps=M("6KoVYK8YDJktnY8KA"), ig="https://www.instagram.com/explore/locations/244530822/ribera-country-club/"),
 dict(name="El Fressco", tel="8095747744", maps=M("1zc7wTCHd74PusgJ8"), ig=IG("elfressco")),
 dict(name="Balcón RD", tel="8293161289", maps=M("ERzypj7jYJS7dXjj6"), ig="https://www.instagram.com/explore/locations/110173861738561/balcon-restaurant/"),
 dict(name="La Tinaja", tel="8095742311", maps=M("7ULaCKXKAPoT96MB6")),
 dict(name="Pelé Kitchen & Grill", tel="+18494727691", maps=M("VYr5n8msnMPaPJbcA"), ig=IG("pelekitchengrill")),
 dict(name="La Baita", tel="8294510379", maps=M("BFM6TEeDyGLqHzmSA"), ig=IG("la_baita")),
 dict(name="Pikota", tel="8092855871", maps=M("hJoS7qEcnMUaUiGP6"), ig=IG("pikotarest")),
 dict(name="Jamaca de Dios Restaurant", tel="+18294526884", maps=M("yU9R3BchGXcyHEQ67"), ig=IG("jamacadediosrestaurant")),
 dict(name="Vista del Campo", tel="8294717305", maps=M("TJmkoCNtMJRQvPrL7"), ig=IG("vistadelcampord")),
 dict(name="Pinar Dorado", tel="8095742127", maps=M("DQiJGzJ25qfATsQi7"), ig=IG("pinardorado")),
 dict(name="Parador Corazón de Jesús", ig=IG("paradorcorazondejesus")),
 dict(name="Plaza Alterra", tel="8095746741", maps="https://goo.gl/maps/Qj1vVNkCXdiwyWvG6", ig=IG("plaza_alterra")),
 dict(name="Café Colao", tel="8297523723", maps=M("sKcep15W1yWRuoqj7"), ig=IG("cafecolao__")),
 dict(name="Tostadohs", tel="+18093658236", maps=M("7cSYy29smRFtBFzP8")),
 dict(name="La Melaza", tel="+18095742659", maps=M("mD3EoaK4cDeMbury9"), ig=IG("lamelazardjarabacoa")),
 dict(name="Serie 50", tel="8095744021", maps="https://goo.gl/maps/ycCj4uSySGTiev4c6", ig=IG("serie50byjarabacoa")),
 dict(name="Pizza & Pepperoni", tel="8095744079", maps=M("SbHsbseuBtQEu8Wb6"), ig=IG("pizzaypepperoni")),
 dict(name="Pizza Getto", tel="8293654490", maps=M("YExt5DrFFSdpcvNw5"), ig=IG("pizzagettojarabacoa"))]
SUPER = [
 dict(name="Súper Colmado Quezada", sub="Tiene delivery a Villa Mi Sueño", star=True, tel="8092054985", maps=M("SQBpphSCm6q1xTZU8")),
 dict(name="Supermercado Jarabacoa", sub="Av. Independencia", tel="8095742780", maps=M("HkotsNJdeBzc3MWo8")),
 dict(name="Supermercado El Cofre", sub="Carretera Principal", tel="8095742309", maps=M("3Ycj9VtaJo2HPJLYA")),
 dict(name="Supermercado El Reguero", sub="Calle Obdulio Jiménez", tel="8093659486", maps=M("S1CJtGQ9x81HwvKV6")),
 dict(name="Mercado Público", sub="Calle Marina Nelson Galán", maps=M("6czhtdTjUsLvZTGi6"))]
TIENDAS = [
 dict(name="Rico Toro", sub="Carnicería y pescadería · tiene delivery", tel="8093658839", maps=M("7CjYvC8zLnLysZqC8")),
 dict(name="Super Carnicería Jarabacoa", sub="Carnicería", tel="8095744848", maps=M("vCHJ2GvP4NVZx1th9")),
 dict(name="Khoury Multicentro", sub="Ferretería", tel="8095747373", maps=M("EsGB8MyzhpW6kk4i7"), ig=IG("khourymulticentro")),
 dict(name="Tienda La Cancha", sub="Artículos varios", tel="8095742466", maps=M("3nMQXVSwTSnQeRnB9")),
 dict(name="Karini Clothing Store", sub="Ropa", tel="8095744418", maps=M("6MzKd7DUB6k9tKMQ8"))]
DIRECTORIO = [
 dict(name="Farmacia San Miguel II", sub="Av. Estela Geraldino No. 17", tel="8095742040", maps=M("HJpVpvMCQ2jHR6qX6")),
 dict(name="Ecofarma", sub="Farmacia · Av. Independencia", maps=M("CqLW4MJKSVaiqoR29")),
 dict(name="Banco BHD", maps=M("qbPgv3JZtM8wAYjx7")),
 dict(name="Banreservas", maps=M("FdRdG54Sji9BevRg6")),
 dict(name="Banco Popular", maps=M("4BohHZD3i4L9h7wZ7")),
 dict(name="Petronan Jarabacoa", sub="Gasolinera · abierta 24 horas", tel="8095742797", maps=M("xhk5XUk26TrtfzXU9")),
 dict(name="Shell", sub="Gasolinera · abierta 24 horas", tel="8095424752", maps=M("nLXRSxQHztkNnscE6")),
 dict(name="Iglesia del Carmen", sub="C. del Carmen, Jarabacoa", tel="8095742559", maps=M("ZgrET7MzBaztVgZB9"))]
RUTA = ["Comenzamos desde el Cruce de Jarabacoa.",
 "Pasarán la Bomba Texaco, Zona Franca, Bayacanes, Arepas de Maíz, La Virgencita, una subida GRANDE, Los Alpes Dominicanos, Parador de Jesús y Buena Vista (¡cuidado!, muchos lo confunden con Jarabacoa) hasta la Estación Shell. Aquí comienza la ruta hasta Villa Mi Sueño.",
 "Al salir de la Estación Shell (siempre camino a Jarabacoa), busquen con cuidado el Cruce del Salto de Jimenoa (muchísimos letreros lo indican) y tomen a la izquierda.",
 "Sigan la carretera hacia el Salto y, en la primera intersección en forma de Y, tomen a la izquierda.",
 "Pasan el Campo de Golf. Llegarán a una T: doblen a la derecha, siempre en dirección al Salto de Jimenoa.",
 "Pasan el Hotel Montaña Azul. Atención: se acerca un cruce que dice Mata de Plátano; ahí tomen la izquierda. (Si siguen derecho llegarán al Salto y tendrán que devolverse.)",
 "Sigan este camino hasta la garita. Pueden preguntar a los guardianes cómo llegar a Villa Mi Sueño o a la casa de Julián y Deysi (¡seguro que les indican!), o seguir solos.",
 "Tomen el Camino del Ébano, la calle principal de Mata de Plátano. Pasan un tanque azul de agua (sigan el camino que gira a la izquierda) y varias casas bonitas hasta Rancho Bariloche.",
 "En Rancho Bariloche (¡ojo, hay un badén bien grande!) doblen a la derecha por el Camino del Nuez.",
 "Sigan derecho por el Camino del Nuez: en la primera intersección giren a la derecha y en la segunda a la izquierda, tomando el Camino del Bambú.",
 "Sigan… sigan… ¡no se desesperen! Al final del Camino del Bambú, la última casa, está Villa Mi Sueño."]
TRAER = ["Pasta de dientes", "Shampoo", "Acondicionador", "Botas de agua o para caminar", "Juegos", "Libros", "Repelente", "Tu comida", "Tu bebida", "Hielo"]
TENEMOS = [("Cocina", ["Estufa", "Horno a gas", "Refrigerador, microondas y bebedero", "Airfryer, licuadora y tostadora", "Horno a leña y Lorena", "Vajilla, tazas, platos y cubiertos", "Accesorios y utensilios de cocina", "Mesa de comedor para 12 personas"]),
 ("Habitaciones", ["6 camas dobles tamaño queen", "6 camas individuales tamaño twin", "Aire acondicionado en 5 habitaciones", "Almohadas, mantas y ropa de cama"]),
 ("Baños", ["7 baños equipados", "Agua caliente", "Toallas y alfombras de baño", "Gel de baño"]),
 ("Exteriores", ["BBQ y sus herramientas", "Mesa de comedor para 8 personas", "Patio privado", "Área para fogata con leña", "Piscina de cloración salina: libre de químicos nocivos", "Jacuzzi con calentador", "Casa del árbol", "Área de juegos", "Espacio para estacionar", "Gazebo", "Mesa de billar"]),
 ("Espacio oficina", ["Escritorio y silla de trabajo"]),
 ("Para bebés", ["Silla para bebé", "Moisés para bebé", "Corral", "Bañito", "Cambiador"])]
AMEN = [("bed", "6 camas queen + 6 twin"), ("snow", "Aire en 5 habitaciones"), ("bath", "7 baños · agua caliente"), ("waves", "Piscina salina"),
 ("sparkles", "Jacuzzi con calentador"), ("flame", "Fogata con leña"), ("grill", "BBQ"), ("pot", "Cocina equipada"),
 ("pizza", "Horno a leña"), ("fork", "Comedor para 12"), ("circle", "Billar"), ("trees", "Casa del árbol"),
 ("dice", "Área de juegos"), ("baby", "Artículos para bebé"), ("car", "Estacionamiento"), ("desk", "Espacio oficina")]
EMERG = ["Centro Médico Jarabacoa", "Hospital Octavia Gautier de Vidal", "Bomberos Buena Vista Jarabacoa", "Bomberos Jarabacoa", "Policía Nacional", "Digesett"]

def subnav(view, items):
    return '<nav class="sub">' + "".join(f'<a href="#{view}:{i}">{e(t)}</a>' for i, t in items) + "</nav>"

# ---------------- vistas ----------------
def v_portada():
    inner = (f'<div class="pt-top"><span class="sello"><i class="mark"></i></span><span class="tg">Welcome book</span></div>'
             f'<div class="pt-bot"><p class="loc">{ic("pin")}Jarabacoa · República Dominicana</p>'
             f'<h1>Villa Mi Sueño</h1><p class="prom">Relax + Enjoy</p>'
             f'<div class="stats"><div><b>12</b><span>camas</span></div><div><b>7</b><span>baños</span></div><div><b>18</b><span>huéspedes</span></div></div>'
             f'<a class="cta" href="#inicio">Abrir guía <span>{ic("arrow")}</span></a></div>')
    return f'<section data-view="portada" class="portada" {fs("bienvenida")}>' + foto("portada", "pt-bg", inner, "exterior de la villa") + "</section>"

def v_inicio():
    host = foto("anfitriones", "retrato", "", "Julián y Deysi")
    return f'''<section data-view="inicio" class="view">
{header("bienvenida", "Bienvenidos", "Bienvenidos a nuestra casa", "Todo lo que necesitas para disfrutar tu estadía, en un solo lugar.")}
<article class="card host" {fs("bienvenida")}>{host}<div class="msg"><div class="firma"><h3>Julián y Deysi</h3><span class="badge">Tus anfitriones</span></div>
<p><b>¡Bienvenido a Villa Mi Sueño!</b> Estamos muy felices de que hayas elegido hospedarte con nosotros. Queremos que te sientas cómodo y como en casa, sin importar la distancia.</p>
<p>Todo el equipo de Villa Mi Sueño y Hospedify te desea una experiencia maravillosa. <b>¡Disfruta cada momento aquí!</b></p>
<details><summary>Acerca de Villa Mi Sueño</summary>
<p>Si le preguntas a Julián y a Deysi qué es Villa Mi Sueño, te dirán que es su rincón especial, un lugar lleno de magia y amor donde han creado recuerdos inolvidables con su familia, especialmente con sus nietos.</p>
<p>Cada rincón de este refugio ha sido pensado con detalle y cuidado, para que te sientas como en casa desde el primer momento. Nos encanta disfrutar de la buena comida, la música, un buen vino, y esos momentos tranquilos con un libro en la mano, acompañados de un cafecito o un chocolate caliente.</p>
<p>Hoy queremos abrirte las puertas de nuestro pequeño paraíso para que tú también puedas vivir momentos únicos, rodeado de la misma calidez y cariño con los que fue creado. ¡Esperamos que te sientas parte de nuestra familia!</p></details></div></article>
{h2("Conéctate", "Wi-Fi", "wifi")}
<article class="card feat wifi" {fs("wifi")}><div class="wh">{chip("wifi", size="l")}<span class="lb acc2">Disponible en toda la villa</span></div>
<div class="cred"><div><span class="lb">Red</span><b>VILLAMIS</b></div><i></i><div><span class="lb">Contraseña</span><b id="pw">Misueno@01</b></div></div>
<button class="copy" data-copy="pw">{ic("copy")}<span>Copiar contraseña</span></button></article>
{nota("el QR del Wi-Fi dice Misueno@01 y el letrero impreso Misueño@1. Confirmar la contraseña real.")}
{h2("A mano", "", "contacto")}
{info("bienvenida", "tel", "Contacto", "Julián Cruz · 1 (809) 697-6946", '<a href="mailto:julian@cruzcid.com">julian@cruzcid.com</a>',
      '<div class="btns"><a class="btn" href="tel:+18096976946">'+ic("tel")+'Llamar</a><a class="btn" href="https://wa.me/18096976946" target="_blank" rel="noopener">'+ic("chat")+'WhatsApp</a><a class="btn" href="mailto:julian@cruzcid.com">'+ic("mail")+'Correo</a></div>')}
{info("bienvenida", "pin", "Ubicación", "Camino del Bambú No. 32", "Mata de Plátano, Jarabacoa",
      '<div class="btns"><a class="btn" href="https://maps.app.goo.gl/7L5uPZCGwBBw8pvBA" target="_blank" rel="noopener">'+ic("map")+'Google Maps</a><a class="btn" href="#casa:ruta">'+ic("ruta")+'Ruta paso a paso</a></div>')}
{nota("confirmar que WhatsApp usa el mismo número que el teléfono.")}
{h2("Emergencias", "", "emergencias")}
<article class="card tint emer" {fs("emergencias")}><div class="tema">{chip("siren", size="m")}<h3>En caso de emergencia</h3></div>
<ul class="rows">{row("<b>Extintores:</b> ubicados en las áreas de circulación.", "shield")}{row("<b>Botiquín:</b> en el cajón inferior del mueble sideboard de la sala.", "shield")}</ul><hr>
<ul class="svc">{"".join(f"<li>{e(x)}</li>" for x in EMERG)}</ul></article>
{nota("faltan los teléfonos y mapas de los servicios de emergencia (no vienen en los enlaces del PDF).")}
{h2("Comparte tu estancia", "", "comparte")}
<article class="card" {fs("comparte")}><div class="tema">{chip("ig", size="m")}<h3>Instagram</h3></div>
<p>Etiqueta <b>#VillaMiSueño</b> y comparte tus momentos favoritos. ¡Nos encanta ver las experiencias de nuestros huéspedes!</p>
<div class="btns"><a class="btn" href="https://www.instagram.com/villa_mi_sueno/" target="_blank" rel="noopener">{ic("ig")}@villa_mi_sueno</a></div><hr>
<div class="tema">{chip("star", size="m")}<h3>Review</h3></div><p>Agradecemos mucho que te tomes el tiempo de evaluarnos. Te mandaremos una breve encuesta a tu salida.</p></article>
<article class="card club" {fs("bienvenida")} id="vuelve"><span class="lb">Vuelve a reservar</span><h3>The Return Stay Club</h3>
<div class="dots"><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i><i></i></div>
<p>Obtén <b>una noche gratis en tu quinta estancia</b>. Cada vez que regreses disfrutarás de más beneficios y descuentos.</p>
<div class="btns"><a class="btn solid" href="mailto:julian@cruzcid.com?subject=Reserva%20Villa%20Mi%20Sue%C3%B1o">{ic("mail")}Escríbenos para reservar</a></div></article>
<p class="pdf"><a href="../assets/VMS-Welcome-Pack.pdf" target="_blank">Ver welcome pack en PDF</a></p>
</section>'''

def v_casa():
    exp = foto("casa", "photo", f'<span class="badge glass">Tu espacio, tu ritmo</span><p class="frase">Días de piscina,<br>noches junto al fuego.</p>', "piscina / terraza")
    amen = "".join(f'<div class="am">{ic(i)}<span>{e(t)}</span></div>' for i, t in AMEN)
    inv = "".join(f"<h4>{e(t)}</h4><ul>" + "".join(f"<li>{e(x)}</li>" for x in l) + "</ul>" for t, l in TENEMOS)
    return f'''<section data-view="casa" class="view">
{header("llegada", "Estadía", "Siéntete en casa", "Horarios, accesos y todo lo que la villa tiene para ti.")}
{subnav("casa", [("llegada", "Llegada"), ("ruta", "Cómo llegar"), ("traer", "Qué traer"), ("debes", "Debes saber"), ("tenemos", "Tenemos para ti"), ("salida", "Antes de irte")])}
{h2("Llegada y salida", "", "llegada")}
<article class="card horario" {fs("llegada")}><div class="gh"><span class="tipo">{ic("in")}Check-in</span><b class="hora">3:00 P.M.</b></div><hr>
{rows(["Si llegas a la hora indicada, alguien del equipo de Villa Mi Sueño te dará la bienvenida y te mostrará todo.", "Si llegas más tarde, te enviaremos a tu teléfono, unas horas antes, el código y las instrucciones para acceder a la casa.", "Si llegas de noche, una linterna te será útil."])}
<p class="small">¿Cambian tus planes de viaje? Contáctanos y haremos lo posible por adaptarnos a tu horario.</p></article>
<article class="card horario" {fs("casa")} id="salida"><div class="gh"><span class="tipo">{ic("out")}Check-out</span><b class="hora">11:00 A.M.</b></div><hr>
{rows([("Apaga las luces y los electrodomésticos.", "ICO-39"), "Saca la basura a los contenedores.", ("Cuelga la llave de la casa junto a la puerta de entrada.", "ICO-37")])}
<p class="small">Hacemos nuestro mejor esfuerzo para acomodar salidas tardías: contáctanos si lo necesitas.</p></article>
{h2("Cómo llegar", "", "ruta")}
<article class="card" {fs("llegada")}><div class="tema">{chip("pin", size="m")}<h3>Camino del Bambú No. 32</h3></div><p>Mata de Plátano, Jarabacoa, R.D.</p>
<div class="btns"><a class="btn solid" href="https://maps.app.goo.gl/7L5uPZCGwBBw8pvBA" target="_blank" rel="noopener">{ic("map")}Abrir en Google Maps</a></div>
<details><summary>Si no carga el GPS: ruta paso a paso</summary><ol class="ruta">{"".join(f"<li>{e(p)}</li>" for p in RUTA)}</ol></details></article>
{h2("Antes de tu llegada", "No olvides traer", "traer")}
<article class="card" {fs("bienvenida")}><div class="tags">{"".join(f"<span>{e(x)}</span>" for x in TRAER)}</div>
<div class="tags plus"><span>Mentalidad de relajación y disfrute :)</span><span>Actitud aventurera</span><span>Conexión con los sentidos</span></div></article>
{h2("Debes saber", "", "debes")}
<article class="card feat" {fs("debes")}>{chip("users", size="l")}<div><span class="lb">Personal de apoyo</span><b>8:00 A.M. – 6:00 P.M.</b><p>Personal dedicado a la cocina, limpieza y asistencia para cualquier necesidad durante tu estancia.</p></div></article>
{info("debes", "ICO-05", "Temperatura y luces", "Disfruta el aire puro de Jarabacoa", "Usa el aire acondicionado solo cuando sea necesario y apaga luces y aire cuando no los uses. Juntos podemos disfrutar y cuidar el planeta.")}
{info("debes", "drop", "Agua", "Dispensador con botellón", "Disponible para tu comodidad.")}
{info("debes", "towel", "Toallas", "Una por huésped registrado", "Se debe devolver la misma cantidad al finalizar la estancia.")}
{info("debes", "bell", "¿Notas algo?", "Avísanos", "Si notas alguna anomalía en la casa, infórmanos y haremos lo posible por solucionarla rápidamente.", tint=True)}
{exp}
{h2("Tenemos para ti", f"{len(AMEN)} destacados", "tenemos")}
<div class="amen" {fs("casa")}>{amen}</div>
<details class="card inv" {fs("casa")}><summary>Ver inventario completo</summary>{inv}</details>
</section>'''

def v_reglas():
    agua = foto("piscina", "photo short", '<span class="lb on">Zonas de agua</span><p class="frase">Disfruta con calma<br>y seguridad.</p>', "piscina y jacuzzi")
    return f'''<section data-view="reglas" class="view">
{header("casa", "Convivencia", "Cuidemos este lugar", "¡Estás a punto de disfrutar de un hogar único! Cuídalo con el mismo cariño que tu propio espacio.")}
{subnav("reglas", [("casa-r", "La casa"), ("piscina", "Piscina y jacuzzi"), ("mascotas", "Mascotas")])}
<article class="card feat cap" {fs("casa")}><div class="cifra"><b>18</b><span>máximo</span></div><div><b>Huéspedes registrados</b><p>Todos los huéspedes deben estar registrados y proporcionar su identificación al menos 48 h antes del check-in.</p></div></article>
{group("casa", "En la casa", "home", [("Respeta el horario antirruidos de Mata de Plátano: de 11:00 P.M. a 7:00 A.M. Máximo 60 dB de día y 50 dB de noche.", "ICO-19"),
   ("No se permiten fiestas, orquestas ni DJs, ni bocinas grandes.", "ICO-32", True), ("Prohibido fumar dentro de la casa.", "ICO-27", True),
   ("No se permiten sustancias ilegales en las instalaciones.", "ICO-33", True), ("No se permiten fotos ni vídeos comerciales sin autorización previa del propietario.", "ICO-25", True),
   ("No muevas los muebles ni les des un uso distinto al diseñado, dentro y fuera.", "sofa", True)], id_="casa-r")}
{group("casa", "Mantenimiento", "key", [("Apaga el aire acondicionado y las luces cuando salgas.", "ICO-04"), ("Respeta los horarios de entrada y salida.", "ICO-31"),
   ("Cuida tus llaves: las llaves perdidas tienen un costo de reemplazo de US$ 50.00.", "ICO-37")])}
{group("casa", "Específicas", "info", [("Villa Mi Sueño es adecuada para niños menores de 12 años, siempre bajo supervisión de un adulto.", "ICO-18"),
   ("No coloques sobre la mesa de billar objetos que no le pertenezcan.", "table", True), ("No instales decoraciones que requieran perforaciones, cinta adhesiva u otros métodos que dañen las superficies.", "decor", True)])}
{agua}
{group("piscina", "Piscina", "waves", [("Ducha obligatoria antes de entrar a la piscina o al jacuzzi.", "ICO-17"), ("Traje de baño obligatorio: no tejidos de algodón.", "ICO-21"),
   ("Niños siempre supervisados por un adulto. Tenemos chalecos salvavidas para los más pequeños.", "ICO-18"),
   ("No hay salvavidas en servicio: usas las instalaciones bajo tu propio riesgo.", "info"),
   ("No correr ni saltar en el área de la piscina.", "ICO-29", True), ("No lanzarse de cabeza a la piscina o al jacuzzi.", "ICO-23", True),
   ("No consumir alimentos en el área.", "ICO-28", True), ("No fumar.", "ICO-27", True), ("No usar vidrio ni objetos pequeños en la piscina.", "ICO-22", True),
   ("Mantén el volumen bajo y evita comportamientos ruidosos.", "ICO-19", True), ("No se permiten mascotas en la piscina ni en el jacuzzi.", "ICO-30", True),
   ("Visitas solo con consentimiento previo del anfitrión.", "users")], dato="4 y 5 pies", id_="piscina")}
{group("piscina", "Jacuzzi, fogata y BBQ", "ICO-13", [("La climatización del jacuzzi está incluida 2 h al día.", "ICO-13"),
   ("Cada 2 h adicionales de calentamiento: US$ 50.00.", "ICO-26"), ("No usar aceites, lociones u otros productos en el jacuzzi.", "drop", True),
   ("Fogata y BBQ disponibles. La leña está incluida; si prefieres carbón, tráelo tú.", "flame"),
   ("Pide al personal el jacuzzi (incluido o adicional), la fogata o el BBQ <b>antes de las 5:00 P.M.</b>", "bell")], dato="2 h incluidas")}
{nota("el PDF en español dice «US$ 50.000» y el inglés «US$50.00». Aquí va US$ 50.00; confirmar.")}
{group("casa", "Mascotas", "ICO-35", [("¡Somos pet friendly! Aceptamos hasta 2 mascotas de tamaño pequeño o mediano.", "ICO-35"),
   ("Maneja los desechos correctamente y mantén limpia el área exterior.", "ICO-36"), ("Mantén vigilada a tu mascota para prevenir accidentes o daños.", "ICO-30"),
   ("No se permiten mascotas en muebles, camas, piscina ni jacuzzi.", "ICO-34", True)], dato="Máximo 2", id_="mascotas")}
</section>'''

def v_explora():
    hero = foto("explora", "photo", f'<span class="badge glass">{ic("trees")}Naturaleza viva</span><div class="txt"><p class="frase">Ríos, saltos<br>y montaña</p><p>Pregunta a tus anfitriones por tiempos de viaje y recomendaciones del día.</p></div>', "paisaje de Jarabacoa")
    av = ""
    for t, icon, trip, lst in AVENTURA:
        tl = f'<a class="mini" href="{trip}" target="_blank" rel="noopener">{ic("trip")}TripAdvisor</a>' if trip else ""
        av += f'<div class="cat"><div class="tema">{chip(icon, size="m")}<h3>{e(t)}</h3>{tl}</div>{places("jarabacoa", lst)}</div>'
    return f'''<section data-view="explora" class="view">
{header("jarabacoa", "Jarabacoa", "Sal a descubrir", "Ríos, montañas y sabores locales: una selección para explorar a tu propio ritmo.")}
{subnav("explora", [("naturaleza", "Naturaleza"), ("aventura", "Aventura"), ("tranquilos", "Planes tranquilos"), ("comer", "Comer y beber"), ("compras", "Compras"), ("directorio", "Directorio")])}
{hero}
{h2("Naturaleza", "", "naturaleza")}{places("jarabacoa", NATURALEZA)}
{h2("Aventura", "Deportes extremos", "aventura")}{av}
{nota("en el PDF varios operadores comparten un mismo bloque de enlaces; se han repartido por orden. Verificar teléfonos y mapas de parapente, buggys y rafting.")}
{h2("Planes tranquilos", "", "tranquilos")}{places("jarabacoa", TRANQUILOS)}
{h2("Comer y beber", f"{len(COMER)} lugares", "comer")}{places("jarabacoa", COMER)}
{h2("Compras", "", "compras")}<div class="cat"><div class="tema">{chip("bag", size="m")}<h3>Supermercados</h3></div>{places("jarabacoa", SUPER)}</div>
<div class="cat"><div class="tema">{chip("bag", size="m")}<h3>Si necesitas algo</h3></div>{places("jarabacoa", TIENDAS)}</div>
{h2("Directorio local", "Cerca de ti", "directorio")}{places("jarabacoa", DIRECTORIO, note="los tres bancos venían con los mapas mezclados en el PDF: verificar BHD, Banreservas y Popular.")}
</section>'''

NAV = [("inicio", "Inicio", "home"), ("casa", "La casa", "key"), ("reglas", "Reglas", "clip"), ("explora", "Explora", "map")]

CSS = r"""
:root{--fondo:#FBF8F1;--tarjeta:#FFFDF8;--linea:#DED8C9;--t2:#6E6C61;--tinta:#272525;--azul:#141F3A;--crema:#F2EDE4;--magenta:#99234E;
--disp:'Philosopher',Georgia,serif;--txt:'Montserrat',system-ui,-apple-system,sans-serif}
*{box-sizing:border-box}html{height:100%;scroll-behavior:smooth;scroll-padding-top:16px}
:root{padding-top:env(safe-area-inset-top,0px)}
body{margin:0;min-height:100%;background:#E9E4DA;font:500 15px/1.5 var(--txt);color:var(--tinta);-webkit-font-smoothing:antialiased}
.app{max-width:480px;margin:0 auto;min-height:100vh;background:var(--fondo);position:relative;box-shadow:0 0 0 1px rgba(0,0,0,.04)}
a{color:inherit}[hidden]{display:none!important}
.view{padding:18px 20px calc(110px + env(safe-area-inset-bottom,0px))}
/* encabezado */
.hd{margin:6px 0 26px}.hd h1{font:700 32px/1.08 var(--disp);margin:10px 0 10px;color:var(--tinta)}.hd p{margin:0;color:var(--t2);font-size:14px}
.eb{display:flex;align-items:center;gap:8px}.eb i{width:22px;height:2px;border-radius:2px;background:var(--acc)}
.eb span,.lb,.badge,.dato,.tipo{font:600 11px/1 var(--txt);letter-spacing:1.6px;text-transform:uppercase}
.eb span{color:var(--ink)}
.sub{display:flex;gap:8px;overflow-x:auto;margin:-8px -20px 22px;padding:2px 20px 6px;scrollbar-width:none}.sub::-webkit-scrollbar{display:none}
.sub a{flex:none;text-decoration:none;font:600 12px var(--txt);padding:8px 13px;border-radius:99px;border:1px solid var(--linea);background:var(--tarjeta)}
.h2{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin:30px 0 12px}
.h2 h2{font:700 24px/1.1 var(--disp);margin:0}.h2 span{font-size:12px;color:var(--t2);font-weight:600}
/* tarjetas */
.card{background:var(--tarjeta);border:1px solid var(--linea);border-radius:20px;padding:18px;margin-bottom:12px}
.card p{margin:8px 0}.card hr{border:0;border-top:1px solid var(--linea);margin:14px 0}
.card.tint{background:var(--tint);border-color:color-mix(in srgb,var(--acc) 35%,transparent)}
.card.feat{background:var(--acc);color:var(--on);border:0;display:flex;gap:14px;align-items:flex-start}
.card.feat .lb{opacity:.75}.card.feat p{opacity:.85;font-size:13.5px;margin:6px 0 0}.card.feat b{display:block;font-size:17px;margin-top:6px}
.card.feat .chip{background:color-mix(in srgb,var(--on) 12%,transparent);color:var(--on)}
.tema{display:flex;align-items:center;gap:10px}.tema h3,.gh h3{font:700 19px/1.15 var(--disp);margin:0}
.gh{display:flex;align-items:center;justify-content:space-between;gap:10px}
.dato{background:var(--chip);color:var(--ink);padding:6px 9px;border-radius:99px;white-space:nowrap}
/* chips e iconos */
.chip{flex:none;display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--chip);color:var(--ink);position:relative}
.chip.m{width:36px;height:36px;border-radius:12px}.chip.l{width:42px;height:42px;border-radius:14px}
.chip .i{width:58%;height:58%}.chip .bi{width:78%;height:78%;object-fit:contain}
.chip.no::after{content:"";position:absolute;left:50%;top:50%;width:118%;height:2.2px;border-radius:2px;background:var(--magenta);transform:translate(-50%,-50%) rotate(-45deg)}
.i{width:18px;height:18px;flex:none}
.rows{list-style:none;margin:0;padding:0;display:grid;gap:12px}.row{display:flex;gap:10px;align-items:flex-start;font-size:14px;line-height:1.45}.row .chip{margin-top:-2px}
/* info card */
.info{display:flex;gap:14px;align-items:flex-start}.info>div{flex:1;min-width:0}.info b{display:block;font-size:15px;font-weight:600;margin-top:5px}
.info p{color:var(--t2);font-size:13.5px;margin:4px 0 0}.info .lb{color:var(--ink)}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.btn{display:inline-flex;align-items:center;gap:7px;text-decoration:none;font:600 13px var(--txt);padding:10px 14px;border-radius:99px;border:1px solid var(--linea);background:var(--fondo);color:var(--tinta)}
.btn .i{width:16px;height:16px}.btn.solid{background:var(--tinta);color:var(--crema);border-color:var(--tinta)}
/* wifi */
.wifi{flex-direction:column;align-items:stretch}.wh{display:flex;justify-content:space-between;align-items:center}
.acc2{color:#EDA23E}.cred{display:flex;gap:14px;margin:18px 0 14px}.cred>div{flex:1}.cred i{width:1px;background:rgba(242,237,228,.18)}
.cred b{font-size:18px;margin-top:6px;letter-spacing:.3px}
.copy{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;border:0;border-radius:14px;padding:12px;background:rgba(242,237,228,.1);color:var(--crema);font:600 13px var(--txt);cursor:pointer}
.copy .i{width:16px;height:16px}
/* anfitriones */
.host{padding:0;overflow:hidden}.host .msg{padding:18px 20px 20px}.firma{display:flex;justify-content:space-between;align-items:center;gap:10px}
.firma h3{font:700 22px var(--disp);margin:0}.badge{background:var(--chip);color:var(--ink);padding:6px 10px;border-radius:99px}
.retrato{height:190px;background:center/cover}
details summary{cursor:pointer;font-weight:600;font-size:13.5px;margin-top:12px;color:var(--ink);list-style:none}
details summary::before{content:"+ "}details[open] summary::before{content:"– "}details summary::-webkit-details-marker{display:none}
/* emergencias */
.emer .tema{margin-bottom:14px}.svc{margin:0;padding:0;list-style:none;display:grid;gap:8px}
.svc li{padding:10px 12px;border-radius:12px;background:var(--tarjeta);font-weight:600;font-size:14px}
/* club */
.club{text-align:center;background:var(--tint)}.club .lb{color:var(--ink)}.club h3{font:700 26px var(--disp);margin:8px 0 14px}
.dots{display:flex;justify-content:center;gap:8px}.dots i{width:30px;height:30px;border-radius:50%;background:color-mix(in srgb,var(--acc) 45%,#fff);display:grid;place-items:center}
.dots i.ok{background:var(--acc)}.dots i.ok::after{content:"";width:9px;height:5px;border-left:2px solid var(--azul);border-bottom:2px solid var(--azul);transform:rotate(-45deg) translate(1px,-1px)}
.club .btns{justify-content:center}
.pdf{text-align:center;font-size:12.5px;margin:22px 0 0}.pdf a{color:var(--t2)}
/* casa */
.horario .tipo{display:flex;align-items:center;gap:8px;color:var(--ink)}.hora{font:700 24px var(--disp)}.small{font-size:13px;color:var(--t2)}
.ruta{margin:12px 0 0;padding-left:20px;display:grid;gap:10px;font-size:14px}
.tags{display:flex;flex-wrap:wrap;gap:8px}.tags span{padding:8px 12px;border-radius:99px;background:var(--fondo);border:1px solid var(--linea);font-size:13px;font-weight:600}
.tags.plus{margin-top:10px}.tags.plus span{background:var(--chip);border-color:transparent;color:var(--ink)}
.amen{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.am{display:flex;align-items:center;gap:10px;padding:13px 12px;border-radius:16px;background:var(--tarjeta);border:1px solid var(--linea);font-size:13px;font-weight:600;line-height:1.25}
.am .i{color:var(--ink)}
.inv{margin-top:12px}.inv summary{margin:0}.inv h4{font:700 16px var(--disp);margin:16px 0 6px}.inv ul{margin:0;padding-left:18px;font-size:14px;color:var(--t2)}
/* fotos */
.photo,.retrato,.pt-bg{position:relative;background-color:var(--azul);background-size:cover;background-position:center}
.photo{height:220px;border-radius:22px;overflow:hidden;margin:26px 0 8px;padding:18px;display:flex;flex-direction:column;justify-content:space-between;color:#fff}
.photo.short{height:170px}.photo>*{position:relative}.vel{position:absolute!important;inset:0;background:linear-gradient(180deg,rgba(20,31,58,.15),rgba(20,31,58,.72))}
.retrato .vel{background:none}
.photo .frase{font:700 25px/1.12 var(--disp);margin:0}.photo .txt p:not(.frase){margin:6px 0 0;font-size:13px;opacity:.85}
.badge.glass{align-self:flex-start;display:inline-flex;gap:6px;align-items:center;background:rgba(255,253,248,.9);color:var(--tinta)}.badge.glass .i{width:13px;height:13px}
.lb.on{color:#EDA23E}
.ph{background-image:repeating-linear-gradient(135deg,rgba(255,255,255,.05) 0 12px,transparent 12px 24px)!important}
.ph::before{content:attr(data-ph);position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:1;font:600 10.5px var(--txt);letter-spacing:1.4px;text-transform:uppercase;color:rgba(242,237,228,.75);border:1px dashed rgba(242,237,228,.4);border-radius:99px;padding:6px 12px;white-space:nowrap}
.retrato.ph::before{top:46%}.photo.ph::before{top:62px;transform:translateX(-50%)}
.cap{align-items:center}.cifra{flex:none;width:76px;height:76px;border-radius:18px;background:rgba(242,237,228,.12);display:grid;place-content:center;text-align:center}
.cifra b{font:700 32px/1 var(--disp)!important;margin:0!important}.cifra span{font:600 10.5px var(--txt);letter-spacing:1.4px;text-transform:uppercase;opacity:.8}
.row .chip{width:30px;height:30px}.row .chip .bi{width:88%;height:88%}
/* explora */
.list{padding:6px 16px}.pl{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid var(--linea)}
.pl:last-child{border-bottom:0}.pn{min-width:0}.pn b{display:block;font-weight:600;font-size:14.5px}.pn small{display:block;color:var(--t2);font-size:12.5px;margin-top:2px}
.pl.star .pn b::after{content:"★";color:var(--ink);margin-left:6px;font-size:12px}
.acts{display:flex;gap:6px;flex:none}.ab{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:var(--chip);color:var(--ink)}
.ab .i{width:17px;height:17px}
.cat{margin-bottom:6px}.cat .tema{margin:16px 0 10px}.cat .tema h3{flex:1}
.mini{display:inline-flex;align-items:center;gap:5px;font:600 11.5px var(--txt);color:var(--ink);text-decoration:none}.mini .i{width:15px;height:15px}
.nota{font-size:12px;line-height:1.45;color:#7a4b00;background:#FFF4DC;border:1px dashed #E3B45C;border-radius:12px;padding:9px 12px;margin:8px 0 14px}
/* portada */
.portada{min-height:100vh;min-height:100svh;display:flex}.pt-bg{flex:1;display:flex;flex-direction:column;justify-content:space-between;padding:22px 24px calc(28px + env(safe-area-inset-bottom,0px));color:#fff}
.pt-bg>*{position:relative}.pt-bg .vel{background:linear-gradient(180deg,rgba(20,31,58,.25),rgba(20,31,58,.1) 35%,rgba(20,31,58,.85))}
.pt-top{display:flex;justify-content:space-between;align-items:center}.tg{font:600 11px var(--txt);letter-spacing:2px;text-transform:uppercase}
.sello{width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.35);background:rgba(20,31,58,.35);display:grid;place-items:center}
.mark{display:block;width:20px;height:27px;background:var(--crema);-webkit-mask:url(../assets/vms_mark.svg) center/contain no-repeat;mask:url(../assets/vms_mark.svg) center/contain no-repeat}
.loc{display:flex;align-items:center;gap:7px;font:600 11px var(--txt);letter-spacing:1.6px;text-transform:uppercase;margin:0}.loc .i{width:15px;height:15px;color:var(--acc)}
.portada h1{font:700 46px/1 var(--disp);margin:16px 0 4px}.prom{font:italic 700 24px var(--disp);color:var(--acc);margin:0 0 22px}
.stats{display:flex;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.08);border-radius:18px;padding:14px 0;margin-bottom:18px;backdrop-filter:blur(6px)}
.stats div{flex:1;text-align:center;border-left:1px solid rgba(255,255,255,.2)}.stats div:first-child{border:0}
.stats b{display:block;font:700 26px var(--disp)}.stats span{font:600 10.5px var(--txt);letter-spacing:1.5px;text-transform:uppercase;opacity:.85}
.cta{display:flex;align-items:center;justify-content:space-between;text-decoration:none;background:var(--tarjeta);color:var(--tinta);font:600 15px var(--txt);padding:10px 10px 10px 22px;border-radius:99px}
.cta span{width:38px;height:38px;border-radius:50%;background:var(--acc);color:var(--azul);display:grid;place-items:center}
/* nav */
.nav{position:fixed;left:50%;transform:translateX(-50%);bottom:0;width:100%;max-width:480px;display:flex;justify-content:space-around;background:rgba(255,253,248,.96);backdrop-filter:blur(10px);border-top:1px solid var(--linea);padding:10px 8px calc(12px + env(safe-area-inset-bottom,0px));z-index:10}
.nav a{display:flex;flex-direction:column;align-items:center;gap:4px;text-decoration:none;font:600 11px var(--txt);color:var(--t2);min-width:70px}
.nav a span{width:46px;height:30px;border-radius:99px;display:grid;place-items:center}.nav a.on{color:var(--tinta)}.nav a.on span{background:color-mix(in srgb,#CCCACA 60%,transparent)}
body[data-v=portada] .nav{display:none}
.toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%);background:var(--tinta);color:var(--crema);font:600 13px var(--txt);padding:10px 16px;border-radius:99px;opacity:0;transition:.2s;pointer-events:none;z-index:20}.toast.show{opacity:1}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""
JS = r"""
const views=[...document.querySelectorAll('[data-view]')];
function go(){const h=decodeURIComponent(location.hash.slice(1))||'portada';const [v,sub]=h.split(':');
 const view=views.find(x=>x.dataset.view===v)||views[0];views.forEach(x=>x.hidden=x!==view);document.body.dataset.v=view.dataset.view;
 document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.v===view.dataset.view));
 const t=sub&&document.getElementById(sub);if(t){t.scrollIntoView();}else{window.scrollTo(0,0);}}
addEventListener('hashchange',go);go();
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{const v=document.getElementById(b.dataset.copy).textContent;
 try{await navigator.clipboard.writeText(v);}catch(e){}const t=document.querySelector('.toast');t.textContent='Contraseña copiada';t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1600);}));
"""

def build():
    shutil.rmtree(OUT, ignore_errors=True)
    for d in ("assets/icons", "assets/fotos", "vms", "vb"): os.makedirs(os.path.join(OUT, d))
    for f in os.listdir(ICO):
        if f.endswith(".svg"):
            s = open(os.path.join(ICO, f), encoding="utf-8").read(); k = f[:-4]
            if k in BBOX:
                x, y, w, h = BBOX[k]; s = re.sub(r'viewBox="[^"]+"', f'viewBox="{x} {y} {w} {h}"', s, count=1)
            open(os.path.join(OUT, "assets", "icons", f), "w", encoding="utf-8").write(s)
    logo = open(os.path.join(R, "00_BRAND", "LOGOS_SVG", "vms_logo.svg"), encoding="utf-8").read()
    shutil.copy(os.path.join(R, "00_BRAND", "LOGOS_SVG", "vms_logo.svg"), os.path.join(OUT, "assets", "vms_logo.svg"))
    paths = re.findall(r'<path fill-rule="nonzero"[^>]*/>', logo)   # casa + rama (sin wordmark)
    open(os.path.join(OUT, "assets", "vms_mark.svg"), "w", encoding="utf-8").write(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="254 346 87 118">' + "".join(paths) + "</svg>")
    shutil.copy(os.path.join(W, "_fuente", "VMS WELCOME PACK-2026_red.pdf"), os.path.join(OUT, "assets", "VMS-Welcome-Pack.pdf"))
    nav = "".join(f'<a href="#{v}" data-v="{v}"><span>{ic(i)}</span>{e(t)}</a>' for v, t, i in NAV)
    page = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<meta name="theme-color" content="#141F3A"><meta name="robots" content="noindex">'
            '<title>Villa Mi Sueño · Tu guía</title><link rel="icon" href="../assets/vms_mark.svg">'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Philosopher:ital,wght@0,700;1,700&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
            f'<style>{CSS}</style></head><body><div class="app">'
            + v_portada() + v_inicio() + v_casa() + v_reglas() + v_explora() +
            f'<nav class="nav" aria-label="Secciones">{nav}</nav><div class="toast" role="status"></div></div><script>{JS}</script></body></html>')
    open(os.path.join(OUT, "vms", "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write('<!doctype html><meta http-equiv="refresh" content="0;url=vms/">')
    shutil.copy(os.path.join(W, "sitio", "vb", "index.html"), os.path.join(OUT, "vb", "index.html")) if os.path.exists(os.path.join(W, "sitio", "vb", "index.html")) else None
    faltan = [s for s in ("portada", "anfitriones", "casa", "piscina", "explora") if not os.path.exists(os.path.join(FOT, s + ".jpg"))]
    print("ok ->", os.path.join(OUT, "vms", "index.html")); print("fotos pendientes:", ", ".join(faltan) or "ninguna")

if __name__ == "__main__":
    build()
