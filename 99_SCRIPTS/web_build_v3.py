"""VMS · Welcome Pack web · v3  —  ESTRUCTURA EXACTA DEL FIGMA "VMS" (5 pantallas), sin añadir secciones.
Lo que no cabe en las zonas del Figma va en HOJAS DE DETALLE (se abren al tocar la zona correspondiente).
Textos: aprobación pendiente de Miguel (propuesta del chat 2026-10-01). Datos y enlaces: reutiliza web_build_v2.py.
Uso:  python3 99_SCRIPTS/web_build_v3.py   ->   08_WELCOME_WEB/sitio_v3/vms/index.html
Modo revisión (muestra pendientes en amarillo): abrir con ?pendientes  ->  vms/?pendientes#inicio
Fotos: 08_WELCOME_WEB/_fuente/fotos/{portada,anfitriones,casa,piscina,explora}.jpg (si falta -> placeholder)."""
import os, sys, re, shutil, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import web_build_v2 as v2
from web_build_v2 import ic, fs, place, acts, tel, NATURALEZA, AVENTURA, TRANQUILOS, COMER, SUPER, TIENDAS, DIRECTORIO, RUTA, TRAER, TENEMOS, EMERG
e = html.escape
R, W = v2.R, v2.W
OUT = os.path.join(W, "sitio_v3"); FOT = v2.FOT

# iconos de línea que usa el Figma (lucide) y no estaban en v2
v2.I.update({
 "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 "cigoff": '<path d="M3 13h11v4H3zM18 13h3v4h-3M17 8c0-2 2-2 2-4M2 2l20 20"/>',
 "armchair": '<path d="M5 11V7a3 3 0 0 1 3-3h8a3 3 0 0 1 3 3v4M3 13a2 2 0 0 1 4 0v2h10v-2a2 2 0 0 1 4 0v5H3zM6 18v2M18 18v2"/>',
 "leaf": '<path d="M5 19C5 9 11 5 20 4c0 9-4 15-14 15zM5 19c3-5 6-8 10-10"/>',
 "upright": '<path d="M7 17L17 7M8 7h9v9"/>',
 "chev": '<path d="M9 6l6 6-6 6"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "housepl": '<path d="M3 11l9-7 9 7v9H3z"/><path d="M12 16s-3-2-3-4a1.5 1.5 0 0 1 3-.5 1.5 1.5 0 0 1 3 .5c0 2-3 4-3 4z"/>',
 "pawprint": '<circle cx="6" cy="10" r="1.8"/><circle cx="10" cy="6" r="1.8"/><circle cx="14" cy="6" r="1.8"/><circle cx="18" cy="10" r="1.8"/><path d="M8 17c0-3 2-5 4-5s4 2 4 5c0 2-2 2-4 2s-4 0-4-2z"/>',
})
CHEV = '<span class="cv">' + ic("chev") + "</span>"

def foto(slot, cls, inner, desc, extra=""):
    src = os.path.join(FOT, slot + ".jpg")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(OUT, "assets", "fotos", slot + ".jpg"))
        return f'<div class="{cls}" {extra} style="background-image:url(../assets/fotos/{slot}.jpg)"><div class="vel"></div>{inner}</div>'
    return f'<div class="{cls} ph" {extra} data-ph="Foto pendiente · {e(desc)}"><div class="vel"></div>{inner}</div>'

def rev(t): return f'<p class="rev"><b>Pendiente:</b> {t}</p>'
def eyebrow(t): return f'<div class="eb"><i></i><span>{e(t)}</span></div>'
def header(fam, sec, title, intro): return f'<header class="hd" {fs(fam)}>{eyebrow(sec)}<h1>{title}</h1><p>{e(intro)}</p></header>'
def stitle(t, det="", sheet="", fam=None):
    d = ""
    if det:
        d = f'<a class="det" href="#" data-sheet="{sheet}">{e(det)}</a>' if sheet else f'<span class="det">{e(det)}</span>'
    return f'<div class="st"{" " + fs(fam) if fam else ""}><h2>{e(t)}</h2>{d}</div>'
def chip(icon, size=""): return f'<span class="chip {size}">{ic(icon)}</span>'
def punto(icon, text): return f'<li class="pt">{chip(icon)}<span>{text}</span></li>'

# ---------------- PANTALLAS (estructura Figma) ----------------
def s_portada():
    inner = (f'<div class="marca"><span class="sello"><i class="mark"></i></span><span class="tipo">Welcome book</span></div>'
             f'<div class="pres"><p class="ubi">{ic("pin")}Jarabacoa · República Dominicana</p>'
             f'<div class="tit"><h1>Villa Mi Sueño</h1><p class="prom">Relax + Enjoy</p></div>'
             f'<div class="datos"><div><b>12</b><span>camas</span></div><div><b>7</b><span>baños</span></div><div><b>18</b><span>huéspedes</span></div></div>'
             f'<a class="abrir" href="#inicio"><span>Abrir guía</span><i>{ic("arrow")}</i></a></div>')
    return f'<section data-view="portada" class="portada" {fs("bienvenida")}>' + foto("portada", "pt-bg", inner, "exterior de la villa") + "</section>"

def s_inicio():
    return f'''<section data-view="inicio" class="view">
{header("bienvenida", "Bienvenidos", "Bienvenidos a nuestra casa", "Todo lo que necesitas para disfrutar tu estadía, en un solo lugar.")}
<article class="card host tap" data-sheet="anfitriones" {fs("bienvenida")}>{foto("anfitriones", "retrato", "", "Julián y Deysi")}
 <div class="msg"><div class="firma"><h3>Julián y Deysi</h3><span class="badge">Tus anfitriones</span></div>
 <p>¡Bienvenido a Villa Mi Sueño! Estamos muy felices de que hayas elegido hospedarte con nosotros. Queremos que te sientas cómodo y como en casa, sin importar la distancia. <span class="more">Leer más</span></p></div></article>
{rev("la foto de los anfitriones del PDF es de baja resolución (684 px). Pedir una mejor.")}
<div class="sec">{stitle("Conéctate", "Wi-Fi")}
 <article class="card wifi" {fs("wifi")}><div class="cab">{chip("wifi", "l")}<span class="estado">Escanea el código para acceder</span></div>
 <div class="cred"><button class="cp" data-copy="VILLAMIS"><span class="lb">Red</span><b>VILLAMIS</b></button><i></i>
 <button class="cp" data-copy="Misueno@01"><span class="lb">Contraseña</span><b>Misueno@01</b></button></div></article>
 {rev("contraseña: el QR dice Misueno@01 y el letrero impreso Misueño@1. Confirmar.")}</div>
<div class="sec">{stitle("A mano")}
 <article class="card info tap" data-sheet="contacto" {fs("bienvenida")}>{chip("tel", "l")}<div><span class="lb">Contacto</span><b>Julián Cruz · 1 (809) 697-6946</b><p>julian@cruzcid.com · Propietario VMS</p></div>{CHEV}</article>
 <article class="card info tap" data-sheet="llegar" {fs("bienvenida")}>{chip("pin", "l")}<div><span class="lb">Ubicación</span><b>Calle Camino del Bambú No. 32</b><p>Mata de Plátano, Jarabacoa</p></div>{CHEV}</article>
 <article class="card info tint tap" data-sheet="emergencias" {fs("emergencias")}>{chip("siren", "l")}<div><span class="lb">Emergencias</span><b class="falta">Teléfono pendiente</b><p>Centro Médico Jarabacoa · Hospital Octavia Gautier de Vidal · Bomberos · Policía · Digesett</p></div>{CHEV}</article>
 {rev("falta el teléfono de emergencias y los de cada servicio.")}</div>
<article class="card seg tint tap" data-sheet="emergencias" {fs("emergencias")}><div class="cab2">{ic("shield")}<h4>En caso de emergencias</h4>{CHEV}</div>
 <ul class="pts">{punto("shield", "El botiquín está en el cajón inferior del mueble sideboard de la sala.")}{punto("flame", "Los extintores están en las áreas de circulación.")}</ul></article>
</section>'''

def s_casa():
    exp = foto("casa", "photo exp", '<span class="badge glass">Tu espacio, tu ritmo</span><p class="frase">Días de piscina,<br>noches junto al fuego.</p>', "piscina o terraza")
    amen = [("bed", "6 camas queen + 6 twin"), ("snow", "Aire en 5 habitaciones"), ("bath", "7 baños con agua caliente"), ("waves", "Piscina salina"),
            ("sparkles", "Jacuzzi con calentador"), ("flame", "Fogata con leña"), ("grill", "BBQ"), ("pot", "Cocina equipada"),
            ("pizza", "Horno a leña y Lorena"), ("fork", "Comedor para 12"), ("circle", "Mesa de billar"), ("trees", "Casa del árbol"),
            ("dice", "Área de juegos"), ("baby", "Artículos para bebé")]
    am = "".join(f'<div class="am">{ic(i)}<span>{e(t)}</span></div>' for i, t in amen)
    def horario(fam, icon, lab, hora, pasos):
        return (f'<article class="card hor tap" data-sheet="llegada" {fs(fam)}><div class="cab"><span class="tipo">{ic(icon)}{lab}</span><b class="hora">{hora}</b></div>'
                f'<hr><ul class="pts">' + "".join(punto("check", p) for p in pasos) + "</ul></article>")
    return f'''<section data-view="casa" class="view">
{header("llegada", "Estadía", "Siéntete en casa", "Horarios, accesos y todo lo que la villa tiene para ti.")}
<div class="sec">{stitle("Check-in / out", "Ver detalles", "llegada", "llegada")}
 {horario("llegada", "in", "Check-in", "3:00 P.M.", ["Si llegas a la hora indicada, el personal de Villa Mi Sueño te dará la bienvenida.", "Si llegas más tarde, te enviaremos el código de acceso a tu teléfono unas horas antes."])}
 {horario("casa", "out", "Check-out", "11:00 A.M.", ["Apaga las luces y los electrodomésticos.", "Saca la basura a los contenedores.", "Cuelga la llave junto a la puerta de entrada."])}</div>
<article class="card feat info tap" data-sheet="debes" {fs("debes")}>{chip("users", "l")}<div><span class="lb">Personal de apoyo</span><b>8:00 A.M. – 6:00 P.M.</b><p>Cocina, limpieza y asistencia para cualquier necesidad durante tu estancia.</p></div>{CHEV}</article>
{exp}
<div class="sec" {fs("casa")}>{stitle("Tenemos para ti", "14 destacados · ver todo", "inventario", "casa")}
 <div class="amen">{am}</div>
 <p class="nota">También tenemos gazebo, patio privado, estacionamiento, espacio de oficina y comedor exterior para 8.</p></div>
</section>'''

def s_reglas():
    def grupo(fam, icon, title, items, dato="", sheet=""):
        d = f'<span class="dato">{e(dato)}</span>' if dato else ""
        return (f'<article class="card grp tap" data-sheet="{sheet}" {fs(fam)}><div class="cab"><div class="tema">{chip(icon, "m")}<h3>{e(title)}</h3></div>{d}{CHEV}</div><hr>'
                '<ul class="pts">' + "".join(punto(i, t) for i, t in items) + "</ul></article>")
    agua = foto("piscina", "photo agua", '<span class="lbl">Zonas de agua</span><p class="frase">Disfruta con calma<br>y seguridad.</p>', "piscina o jacuzzi")
    return f'''<section data-view="reglas" class="view">
{header("casa", "Convivencia", "Cuidemos este lugar", "¡Estás a punto de disfrutar de un hogar único! Cuídalo con el mismo cariño que tu propio espacio.")}
<article class="card feat cap tap" data-sheet="reglas-casa" {fs("casa")}><div class="cifra"><b>18</b><span>máximo</span></div><div class="cond"><b>Huéspedes registrados</b><p>Identificación de todos al menos 48 h antes del check-in.</p></div></article>
{grupo("casa", "housepl", "En la casa", [("music", "No se permiten fiestas, orquestas ni DJs."), ("moon", "Horario antirruidos: 11:00 P.M. – 7:00 A.M."), ("cigoff", "Prohibido fumar dentro de la casa."), ("armchair", "No mover los muebles ni darles otro uso."), ("key", "Llaves perdidas: US$ 50.00 de reposición.")], sheet="reglas-casa")}
{agua}
{rev("no hay foto nítida de la piscina en el PDF: hace falta una.")}
{grupo("piscina", "waves", "Piscina", [("check", "Ducha previa y traje de baño (no algodón) obligatorios."), ("check", "No hay salvavidas: uso bajo tu propio riesgo."), ("check", "Niños siempre supervisados; hay chalecos salvavidas."), ("check", "No lanzarse de cabeza, correr, comer, fumar ni usar vidrio.")], "4 y 5 pies", "reglas-piscina")}
{grupo("piscina", "bath", "Jacuzzi", [("check", "Calentamiento incluido 2 h al día; cada 2 h extra, US$ 50.00."), ("check", "Sin aceites, lociones ni otros productos."), ("check", "Pide jacuzzi, fogata o BBQ al personal antes de las 5:00 P.M.")], "2 h incluidas", "reglas-piscina")}
{rev("el PDF en español dice US$ 50.000 y el inglés US$50.00: va US$ 50.00, confirmar.")}
{grupo("casa", "pawprint", "Mascotas", [("check", "Somos pet friendly: mascotas pequeñas o medianas."), ("check", "No en muebles, camas, piscina ni jacuzzi."), ("check", "Recoge sus desechos y mantenlas vigiladas.")], "Máximo 2", "reglas-mascotas")}
</section>'''

def s_explora():
    dest = foto("explora", "photo dest", f'<span class="badge glass">{ic("leaf")}Naturaleza viva</span><div class="txt"><p class="frase">Saltos, ríos y montaña</p><p>El balneario del río Camú está a menos de 3 km, dentro de Mata de Plátano. En la foto, el Salto Jimenoa.</p></div>', "Jarabacoa", 'data-sheet="naturaleza"')
    def cat(icon, title, items, sheet, tint=False):
        return (f'<article class="card cat tap{" tint" if tint else ""}" data-sheet="{sheet}" {fs("jarabacoa")}><div class="cab">{chip(icon, "m")}<h3>{e(title)}</h3>{CHEV}</div>'
                '<div class="ops">' + "".join(f'<span class="lugar">{ic("pin")}{e(x)}</span>' for x in items) + "</div></article>")
    rest = ["Herbes Farm to Table", "Cayena by María Marte", "Jamaca de Dios", "El Fressco", "Ribera Country Club", "Pizza & Pepperoni"]
    dirs = [("Súper Colmado Quezada", "Delivery a VMS"), ("Supermercado Jarabacoa", "Supermercado"), ("El Cofre", "Supermercado"), ("Rico Toro", "Carnicería · delivery"),
            ("Ecofarma", "Farmacia"), ("San Miguel II", "Farmacia"), ("Petronan", "Gasolinera 24 h"), ("Shell", "Gasolinera 24 h")]
    return f'''<section data-view="explora" class="view">
{header("jarabacoa", "Jarabacoa", "Qué hacer", "Ríos, montañas y sabores locales: una selección para explorar a tu propio ritmo.")}
{dest.replace('class="photo dest', 'class="photo dest tap')}
<div class="sec">{stitle("Experiencias", "Para todos")}
 {cat("trees", "Naturaleza", ["Río Camú", "Salto Jimenoa", "Salto Baiguate", "La Confluencia"], "naturaleza")}
 {cat("mountain", "Aventura", ["Parapente", "Buggys y four wheels", "Rafting y tubing", "Senderismo", "Mountain bike"], "aventura", True)}
 {cat("sun", "Planes tranquilos", ["Paseo a caballo", "Rancho Miel RD", "Rancho Bariloche", "Helados Ivon"], "tranquilos")}</div>
<div class="sec" {fs("jarabacoa")}>{stitle("Dónde comer", "Ver los 20", "comer", "jarabacoa")}
 <div class="card rest" {fs("jarabacoa")}>''' + "".join(f'<a class="rr" href="#" data-sheet="comer"><span>{e(r)}</span>{ic("upright")}</a>' for r in rest) + f'''</div></div>
<div class="sec">{stitle("Directorio local", "Ver todo", "directorio", "jarabacoa")}
 <div class="card dir" {fs("jarabacoa")}>''' + "".join(f'<a class="dr" href="#" data-sheet="directorio"><b>{e(n)}</b><span>{e(t)}</span></a>' for n, t in dirs) + '''</div></div>
</section>'''

# ---------------- HOJAS DE DETALLE (contenido del PDF que no cabe en las zonas) ----------------
def lst(items): return "<ul class='ul'>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def blk(t, body): return f'<div class="blk"><h4>{e(t)}</h4>{body}</div>'
def plist(lst_): return '<div class="card list">' + "".join(place(**p) for p in lst_) + "</div>"
def btn(href, icon, label, solid=False, ext=True):
    return f'<a class="btn{" solid" if solid else ""}" href="{e(href)}"{" target=_blank rel=noopener" if ext else ""}>{ic(icon)}{e(label)}</a>'
MAPS_VMS = "https://maps.app.goo.gl/7L5uPZCGwBBw8pvBA"

SHEETS = {
 "anfitriones": ("bienvenida", "Tus anfitriones", "Julián y Deysi",
   "<p>¡Bienvenido a Villa Mi Sueño! Estamos muy felices de que hayas elegido hospedarte con nosotros. Queremos que te sientas cómodo y como en casa, sin importar la distancia.</p>"
   "<p>Todo el equipo de Villa Mi Sueño y Hospedify te desea una experiencia maravillosa. <b>¡Disfruta cada momento aquí!</b></p>"
   + blk("Acerca de Villa Mi Sueño", "<p>Si le preguntas a Julián y a Deysi qué es Villa Mi Sueño, te dirán que es su rincón especial, un lugar lleno de magia y amor donde han creado recuerdos inolvidables con su familia, especialmente con sus nietos.</p>"
     "<p>Cada rincón de este refugio ha sido pensado con detalle y cuidado, para que te sientas como en casa desde el primer momento. Nos encanta disfrutar de la buena comida, la música, un buen vino, y esos momentos tranquilos con un libro en la mano, acompañados de un cafecito o un chocolate caliente.</p>"
     "<p>Hoy queremos abrirte las puertas de nuestro pequeño paraíso para que tú también puedas vivir momentos únicos, rodeado de la misma calidez y cariño con los que fue creado. ¡Esperamos que te sientas parte de nuestra familia y que disfrutes cada instante aquí!</p>")
   + blk("Comparte tu estancia", "<p>Etiqueta <b>#VillaMiSueño</b> y comparte tus momentos favoritos con nosotros. ¡Nos encanta ver las experiencias de nuestros huéspedes!</p><div class='btns'>" + btn("https://www.instagram.com/villa_mi_sueno/", "ig", "@villa_mi_sueno") + "</div>"
     "<p>Agradecemos mucho a nuestros huéspedes por tomarse el tiempo de evaluarnos. Te mandamos una breve encuesta a tu salida.</p>")
   + blk("The Return Stay Club", "<div class='dots'><i class='ok'></i><i class='ok'></i><i class='ok'></i><i class='ok'></i><i></i></div><p>Obtén <b>una noche gratis en tu quinta estancia</b>. Cada vez que regreses disfrutarás de aún más beneficios y descuentos.</p><div class='btns'>"
     + btn("mailto:julian@cruzcid.com?subject=Reserva%20Villa%20Mi%20Sue%C3%B1o", "mail", "Escríbenos: julian@cruzcid.com", True, False) + "</div>")),
 "contacto": ("bienvenida", "Contacto", "Julián Cruz Herasme",
   "<p>Propietario de Villa Mi Sueño. Escríbenos o llámanos para lo que necesites.</p><div class='btns col'>"
   + btn("tel:+18096976946", "tel", "Llamar · 1 (809) 697-6946", True, False) + btn("https://wa.me/18096976946", "chat", "WhatsApp") + btn("mailto:julian@cruzcid.com", "mail", "julian@cruzcid.com", ext=False) + "</div>"
   + rev("confirmar que WhatsApp usa el mismo número.")),
 "llegar": ("llegada", "Cómo llegar", "Ruta a Villa Mi Sueño",
   "<p><b>Calle Camino del Bambú No. 32, Mata de Plátano, Jarabacoa, R.D.</b></p><div class='btns'>" + btn(MAPS_VMS, "map", "Abrir en Google Maps", True) + "</div>"
   + blk("Si no carga el GPS", "<p>No importa: sigue las instrucciones al pie de la letra.</p><ol class='ruta'>" + "".join(f"<li>{e(p)}</li>" for p in RUTA) + "</ol>")),
 "emergencias": ("emergencias", "En caso de", "Emergencias",
   blk("En la casa", lst(["<b>Extintores:</b> están ubicados en las áreas de circulación.", "<b>Botiquín:</b> en el cajón inferior del mueble sideboard de la sala."]))
   + blk("Servicios", '<div class="card list">' + "".join(f'<div class="pl"><div class="pn"><b>{e(x)}</b><small class="falta">Teléfono y mapa pendientes</small></div></div>' for x in EMERG) + "</div>")
   + rev("los teléfonos y mapas de los servicios de emergencia no vienen en los enlaces del PDF.")),
 "llegada": ("llegada", "Check-in / out", "Llegada y salida",
   blk("Check-in · 3:00 P.M.", lst(["Si llegas a la hora indicada, un personal de Villa Mi Sueño te dará la bienvenida y te mostrará todo.", "Si llegas más tarde, te enviaremos a tu teléfono, unas horas antes, el código para acceder a la casa.", "Si llegas en la oscuridad, una linterna te será útil.", "Sabemos que los planes de viaje pueden cambiar. Si necesitas ajustar tu hora de llegada, contáctanos y haremos lo posible por adaptarnos a tu horario."]))
   + blk("Check-out · 11:00 A.M.", lst(["Apaga las luces y los electrodomésticos.", "Saca la basura a los contenedores.", "Cuelga la llave de la casa junto a la puerta de entrada.", "Hacemos nuestro mejor esfuerzo para acomodar salidas tardías, así que contáctanos si lo necesitas."]))
   + blk("Antes de tu llegada · No olvides traer", '<div class="tags">' + "".join(f"<span>{e(x)}</span>" for x in TRAER) + '</div><div class="tags plus"><span>Mentalidad de relajación y disfrute :)</span><span>Actitud aventurera</span><span>Conexión con los sentidos</span></div>')
   + "<div class='btns'>" + btn("#", "map", "Cómo llegar · ruta paso a paso", ext=False).replace('href="#"', 'href="#" data-sheet="llegar"') + "</div>"),
 "debes": ("debes", "Debes saber", "Para una estancia tranquila",
   blk("Personal de apoyo", "<p>Para asegurar una estadía placentera, ofrecemos personal dedicado a la cocina, limpieza y asistencia para cualquier necesidad que pueda surgir durante tu estancia. Su horario es de 8:00 A.M. a 6:00 P.M.</p>")
   + blk("Temperatura y luces", "<p>Para cuidar el medio ambiente y ahorrar energía, te invitamos a disfrutar del aire puro de Jarabacoa y usar el aire acondicionado solo cuando sea necesario. Apaga las luces y el aire cuando no los uses. Juntos podemos disfrutar y cuidar el planeta.</p>")
   + blk("Agua", "<p>Disponemos de un dispensador con un botellón de agua para tu comodidad.</p>")
   + blk("Toallas", "<p>Se proporcionará una toalla por cada huésped registrado, y se deberá devolver la misma cantidad al finalizar la estancia.</p>")
   + blk("¿Notas algo?", "<p>Si notas alguna anomalía o situación que requiera atención en la casa, infórmanos y haremos lo posible por solucionarla rápidamente.</p>")),
 "inventario": ("casa", "Tenemos para ti", "Todo lo que hay en la villa", "".join(blk(t, lst([e(x) for x in l])) for t, l in TENEMOS)),
 "reglas-casa": ("casa", "Reglas", "Reglas de la casa",
   blk("Generales", lst(["No se permiten fiestas (no orquestas ni DJs).", "Prohibido fumar dentro de la casa.", "No se permiten sustancias ilegales en las instalaciones.", "Todos los huéspedes deben estar registrados y proporcionar su identificación al menos 48 h antes del check-in.", "Máximo de 18 huéspedes."]))
   + blk("Comportamiento", lst(["No se permiten fotografías ni vídeos comerciales sin previa autorización del propietario.", "Respetar el horario «antirruidos» de la comunidad de Mata de Plátano, de 11:00 P.M. a 7:00 A.M., y en todo momento los niveles de decibeles permitidos por la legislación nacional (no exceder 60 dB de día y 50 dB de noche). No se permiten bocinas grandes.", "No mover los muebles ni darles un uso distinto al diseñado, tanto en interiores como en exteriores."]))
   + blk("Mantenimiento", lst(["Apaga el aire acondicionado y las luces cuando salgas.", "Respeta los horarios de entrada y salida.", "Cuida tus llaves: las llaves perdidas tienen un costo de reemplazo de US$ 50.00."]))
   + blk("Específicas", lst(["Villa Mi Sueño es adecuada para niños menores de 12 años, que deben estar bajo supervisión de un adulto en todo momento.", "No coloques sobre la mesa de billar objetos que no le pertenezcan.", "No se permite instalar decoraciones que requieran perforaciones, cinta adhesiva u otros métodos que dañen las superficies."]))),
 "reglas-piscina": ("piscina", "Reglas", "Piscina y jacuzzi",
   blk("Generales", lst(["Profundidad de la piscina: 4 y 5 pies.", "Ducha obligatoria antes de entrar a la piscina o jacuzzi.", "Traje de baño obligatorio: no tejidos de algodón.", "No hay personal salvavidas en servicio. Los huéspedes usan las instalaciones bajo su propio riesgo.", "Los niños deben ser supervisados por un adulto en todo momento. Tenemos chalecos salvavidas disponibles para los más pequeños."]))
   + blk("Comportamiento", lst(["No correr ni saltar en el área de la piscina.", "No lanzarse de cabeza a la piscina o jacuzzi.", "No consumir alimentos en el área.", "No fumar.", "No usar vidrio ni objetos pequeños dentro de la piscina.", "No usar aceites, lociones u otros productos en el jacuzzi.", "Mantener el volumen bajo y evitar comportamientos ruidosos.", "No se permiten mascotas en la piscina o jacuzzi.", "Visitas solo con consentimiento previo del anfitrión."]))
   + blk("Adicionales", lst(["El precio incluye la climatización del jacuzzi por 2 h diarias. Si quieres calentarlo más tiempo, cada 2 h adicionales cuestan US$ 50.00. Tanto el calentamiento incluido como el adicional deben notificarse al personal antes de las 5:00 P.M.", "Tenemos disponible fogata y BBQ. La leña está incluida en el precio; si prefieres usar carbón, debes traerlo. Solicita la fogata o el BBQ al personal antes de las 5:00 P.M."]))),
 "reglas-mascotas": ("casa", "Somos pet friendly", "Mascotas",
   "<p>¡Damos la bienvenida a tus mascotas y esperamos que se sientan también como en casa! Para garantizar una estancia estupenda para todos, aquí tienes algunos recordatorios para mantener nuestro espacio impecable para futuros huéspedes.</p>"
   + lst(["Aceptamos con gusto hasta un máximo de 2 mascotas de tamaño pequeño y mediano.", "No se permiten mascotas en los muebles, camas, piscina o jacuzzi.", "Asegúrate de manejar los desechos correctamente y mantener el área exterior limpia.", "Mantén vigilada a tu mascota para prevenir accidentes o daños a la propiedad."])),
 "naturaleza": ("jarabacoa", "Qué hacer", "Naturaleza", "<p>Si buscas conectar con la naturaleza, Jarabacoa te ofrece estos espacios para tu disfrute.</p>" + plist(NATURALEZA)),
 "aventura": ("jarabacoa", "Qué hacer", "Aventura",
   "<p>Si buscas aventura y deportes extremos, Jarabacoa te ofrece:</p>" + "".join(blk(t, plist(l) + (f"<div class='btns'>{btn(tr, 'trip', 'Ver en TripAdvisor')}</div>" if tr else "")) for t, _i, tr, l in AVENTURA)
   + rev("en el PDF varios operadores comparten un mismo bloque de enlaces; se han repartido por orden. Verificar.")),
 "tranquilos": ("jarabacoa", "Qué hacer", "Planes tranquilos", "<p>Si buscas un plan menos extremo:</p>" + plist(TRANQUILOS)),
 "comer": ("jarabacoa", "Jarabacoa", "Dónde comer y beber", plist(COMER)),
 "directorio": ("jarabacoa", "Jarabacoa", "Directorio local",
   blk("Supermercados y colmado", plist(SUPER)) + blk("Si necesitas algo", plist(TIENDAS)) + blk("Farmacias, bancos y servicios", plist(DIRECTORIO))
   + rev("los tres bancos venían con los mapas mezclados en el PDF: verificar.")),
}
def sheets():
    out = ""
    for k, (fam, eb, title, body) in SHEETS.items():
        out += (f'<div class="sheet" id="sh-{k}" role="dialog" aria-modal="true" aria-label="{e(title)}" hidden {fs(fam)}><div class="panel">'
                f'<div class="sh-h"><div>{eyebrow(eb)}<h2>{e(title)}</h2></div><button class="x" aria-label="Cerrar">{ic("x")}</button></div>'
                f'<div class="sh-b">{body}</div></div></div>')
    return out

NAV = [("inicio", "Inicio", "home"), ("casa", "La casa", "key"), ("reglas", "Reglas", "clip"), ("explora", "Explora", "map")]

CSS = r"""
:root{--fondo:#FBF8F1;--tarjeta:#FFFDF8;--linea:#DED8C9;--t2:#6E6C61;--tinta:#272525;--azul:#141F3A;--crema:#F2EDE4;--naranja:#EDA23E;
--disp:'Philosopher',Georgia,serif;--txt:'Montserrat',system-ui,-apple-system,sans-serif}
*{box-sizing:border-box}html{height:100%;scroll-padding-top:16px}:root{padding-top:env(safe-area-inset-top,0px)}
body{margin:0;min-height:100%;background:#E9E4DA;font:500 14px/1.45 var(--txt);color:var(--tinta);-webkit-font-smoothing:antialiased}
body.lock{overflow:hidden}
.app{max-width:430px;margin:0 auto;min-height:100vh;background:var(--fondo);position:relative}
a{color:inherit}button{font:inherit;color:inherit}[hidden]{display:none!important}
.view{padding:14px 20px calc(104px + env(safe-area-inset-bottom,0px))}
.i{width:18px;height:18px;flex:none}
/* encabezado */
.hd{margin-bottom:28px}.eb{display:flex;align-items:center;gap:8px}.eb i{width:22px;height:2px;border-radius:2px;background:var(--acc)}
.eb span,.lb,.badge,.dato,.tipo,.det-c{font:600 10.5px/1 var(--txt);letter-spacing:1.6px;text-transform:uppercase}
.eb span{color:var(--ink)}
.hd h1{font:700 31px/1.12 var(--disp);margin:9px 0 9px}.hd p{margin:0;color:var(--t2);font-size:14px}
.sec{margin-bottom:28px}.st{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:12px}
.st h2{font:700 24px/1.15 var(--disp);margin:0}.det{font-size:12px;font-weight:600;color:var(--ink);text-decoration:none;white-space:nowrap}
a.det::after{content:" ›"}
/* tarjeta base */
.card{background:var(--tarjeta);border:1px solid var(--linea);border-radius:20px;padding:18px;margin-bottom:12px;position:relative}
.card p{margin:0}.card hr{border:0;border-top:1px solid var(--linea);margin:14px 0}
.tint{background:var(--tint);border-color:color-mix(in srgb,var(--acc) 30%,transparent)}
.tap{cursor:pointer;transition:transform .12s}.tap:active{transform:scale(.985)}
.cv{color:var(--t2);display:grid;place-items:center;margin-left:auto}.cv .i{width:16px;height:16px}
.chip{flex:none;display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--chip);color:var(--ink)}
.chip .i{width:13px;height:13px}.chip.m{width:36px;height:36px;border-radius:12px}.chip.m .i{width:18px;height:18px}
.chip.l{width:38px;height:38px;border-radius:12px}.chip.l .i{width:19px;height:19px}
.pts{list-style:none;margin:0;padding:0;display:grid;gap:11px}.pt{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;line-height:1.4}
.pt>span:last-child{padding-top:3px}
/* inicio */
.host{padding:0;overflow:hidden}.retrato{position:relative;height:190px;background:var(--azul) center 30%/cover}.retrato .vel{background:none}.msg{padding:20px}
.firma{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px}.firma h3{font:700 22px var(--disp);margin:0}
.badge{background:var(--chip);color:var(--ink);padding:6px 10px;border-radius:99px;white-space:nowrap}
.msg p{font-size:14px;line-height:1.5}.more{font-weight:600;color:var(--ink);white-space:nowrap}.more::after{content:" ›"}
.wifi{background:var(--acc);color:var(--on);border:0;padding:20px}.wifi .chip{background:rgba(242,237,228,.1);color:var(--on)}
.wifi .cab{display:flex;justify-content:space-between;align-items:center;gap:10px}.estado{font:600 10.5px var(--txt);letter-spacing:1.4px;text-transform:uppercase;color:var(--naranja);text-align:right}
.cred{display:flex;gap:12px;margin-top:18px}.cred i{width:1px;background:rgba(242,237,228,.16)}
.cp{flex:1;text-align:left;background:none;border:0;padding:0;cursor:pointer}.cp .lb{opacity:.6;display:block}.cp b{display:block;font-size:16px;margin-top:6px}
.cp b::after{content:"";display:inline-block;width:12px;height:12px;margin-left:8px;vertical-align:-1px;opacity:.55;background:currentColor;-webkit-mask:var(--copy) center/contain no-repeat;mask:var(--copy) center/contain no-repeat}
.info{display:flex;gap:14px;align-items:flex-start;padding:16px}.info>div{flex:1;min-width:0}.info .lb{color:var(--ink)}
.info b{display:block;font-size:14.5px;font-weight:600;margin-top:5px}.info p{color:var(--t2);font-size:12.5px;margin-top:4px}
.info .cv{align-self:center}.falta{color:#9E1B14!important;font-style:italic}
.seg{padding:16px 18px}.cab2{display:flex;align-items:center;gap:9px;color:var(--ink);margin-bottom:12px}.cab2 h4{margin:0;font-size:13.5px;font-weight:600;color:var(--tinta)}
/* casa */
.hor .cab{display:flex;justify-content:space-between;align-items:center}.tipo{display:flex;align-items:center;gap:8px;color:var(--ink)}.tipo .i{width:17px;height:17px}
.hora{font:700 24px var(--disp)}
.feat{background:var(--acc);color:var(--on);border:0}.feat .lb{color:var(--on);opacity:.75}.feat p{color:var(--on);opacity:.85}
.feat .chip{background:color-mix(in srgb,var(--on) 12%,transparent);color:var(--on)}.feat .cv{color:var(--on);opacity:.6}
.photo{position:relative;border-radius:22px;overflow:hidden;margin:0 0 28px;padding:18px;display:flex;flex-direction:column;justify-content:space-between;color:#fff;background:var(--azul) center/cover}
.photo>*{position:relative}.vel{position:absolute!important;inset:0;background:linear-gradient(180deg,rgba(20,31,58,.12),rgba(20,31,58,.7))}
.exp{height:214px}.agua{height:164px}.dest{height:245px}
.frase{font:700 24px/1.15 var(--disp)!important;margin:0}
.badge.glass{align-self:flex-start;display:inline-flex;align-items:center;gap:6px;background:rgba(255,253,248,.88);color:var(--tinta)}.badge.glass .i{width:13px;height:13px}
.lbl{font:600 10.5px var(--txt);letter-spacing:1.6px;text-transform:uppercase;color:var(--naranja)}
.dest .txt p:not(.frase){font-size:12.5px;opacity:.82;margin-top:6px}
.amen{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.am{display:flex;align-items:center;gap:10px;min-height:46px;padding:9px 12px;border-radius:14px;background:var(--tarjeta);border:1px solid var(--linea);font-size:12.5px;font-weight:600;line-height:1.25}
.am .i{color:var(--ink);width:16px;height:16px}
.nota{color:var(--t2);font-size:12.5px;margin:14px 0 0}
/* reglas */
.cap{display:flex;gap:16px;align-items:center}.cifra{flex:none;width:74px;height:74px;border-radius:18px;background:rgba(242,237,228,.1);display:grid;place-content:center;text-align:center}
.cifra b{font:700 32px/1 var(--disp)}.cifra span{font:600 10px var(--txt);letter-spacing:1.4px;text-transform:uppercase;opacity:.75;margin-top:3px}
.cond b{font-size:15px}.cond p{font-size:12.5px;margin-top:5px}
.grp .cab{display:flex;align-items:center;gap:10px}.tema{display:flex;align-items:center;gap:10px}.tema h3,.cat h3{font:700 19px var(--disp);margin:0}
.dato{margin-left:auto;background:var(--chip);color:var(--ink);padding:6px 9px;border-radius:99px;white-space:nowrap}.dato+.cv{margin-left:4px}
/* explora */
.cat .cab{display:flex;align-items:center;gap:10px;margin-bottom:14px}.ops{display:grid;gap:9px;justify-items:start}
.lugar{display:inline-flex;align-items:center;gap:8px;min-width:165px;height:42px;padding:0 16px 0 11px;border-radius:99px;background:var(--tarjeta);border:1px solid var(--linea);font-weight:600;font-size:13.5px}
.lugar .i{width:15px;height:15px;color:var(--ink)}
.rest{background:var(--acc);border:0;padding:8px 16px}.rr{display:flex;justify-content:space-between;align-items:center;height:38px;color:#fff;text-decoration:none;font-weight:600;border-bottom:1px solid rgba(255,255,255,.12)}
.rr:last-child{border:0}.rr .i{width:15px;height:15px;color:var(--naranja)}
.dir{padding:6px 16px}.dr{display:flex;justify-content:space-between;align-items:center;gap:10px;height:36px;text-decoration:none;border-bottom:1px solid var(--linea)}.dr:last-child{border:0}
.dr b{font-weight:600;font-size:13.5px}.dr span{font:600 10px var(--txt);letter-spacing:1.3px;text-transform:uppercase;color:var(--ink);text-align:right}
/* fotos placeholder */
.ph{background-image:repeating-linear-gradient(135deg,rgba(255,255,255,.05) 0 12px,transparent 12px 24px)!important}
.ph::before{content:attr(data-ph);position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:1;font:600 10px var(--txt);letter-spacing:1.3px;text-transform:uppercase;color:rgba(242,237,228,.8);border:1px dashed rgba(242,237,228,.45);border-radius:99px;padding:6px 12px;white-space:nowrap}
.photo.ph::before{top:40%}
/* portada */
.portada{min-height:100vh;min-height:100svh;display:flex}.pt-bg{flex:1;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:20px 24px calc(28px + env(safe-area-inset-bottom,0px));color:#fff;background:var(--azul) center/cover}
.pt-bg>*{position:relative}.pt-bg .vel{background:linear-gradient(180deg,rgba(20,31,58,.35),rgba(20,31,58,.05) 30%,rgba(20,31,58,.2) 55%,rgba(20,31,58,.88))}
.marca{display:flex;justify-content:space-between;align-items:center}.tipo-g,.marca .tipo{font:600 11px var(--txt);letter-spacing:2px;text-transform:uppercase;color:#fff}
.sello{width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.35);background:rgba(20,31,58,.35);display:grid;place-items:center}
.mark{display:block;width:19px;height:26px;background:var(--crema);-webkit-mask:url(../assets/vms_mark.svg) center/contain no-repeat;mask:url(../assets/vms_mark.svg) center/contain no-repeat}
.ubi{display:flex;align-items:center;gap:7px;font:600 10.5px var(--txt);letter-spacing:1.6px;text-transform:uppercase;margin:0}.ubi .i{width:14px;height:14px;color:var(--acc)}
.tit h1{font:700 46px/1.02 var(--disp);margin:18px 0 4px}.prom{font:italic 700 24px var(--disp);color:var(--acc);margin:0 0 20px}
.datos{display:flex;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.08);border-radius:18px;padding:15px 0;margin-bottom:20px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.datos div{flex:1;text-align:center;border-left:1px solid rgba(255,255,255,.2)}.datos div:first-child{border:0}
.datos b{display:block;font:700 26px var(--disp)}.datos span{font:600 10px var(--txt);letter-spacing:1.5px;text-transform:uppercase;opacity:.85}
.abrir{display:flex;align-items:center;justify-content:space-between;text-decoration:none;background:var(--tarjeta);color:var(--tinta);font:600 15px var(--txt);padding:10px 10px 10px 22px;border-radius:99px}
.abrir i{width:36px;height:36px;border-radius:50%;background:var(--acc);color:var(--azul);display:grid;place-items:center}
/* nav */
.nav{position:fixed;left:50%;transform:translateX(-50%);bottom:0;width:100%;max-width:430px;display:flex;justify-content:space-around;background:rgba(255,253,248,.96);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-top:1px solid var(--linea);padding:12px 8px calc(12px + env(safe-area-inset-bottom,0px));z-index:10}
.nav a{display:flex;flex-direction:column;align-items:center;gap:4px;width:74px;text-decoration:none;font:600 11px var(--txt);color:var(--t2)}
.nav a span{width:42px;height:28px;border-radius:99px;display:grid;place-items:center}.nav a.on{color:var(--tinta)}.nav a.on span{background:color-mix(in srgb,#CCCACA 60%,transparent)}
body[data-v=portada] .nav{display:none}
/* hojas */
.sheet{position:fixed;inset:0;z-index:30;display:flex;align-items:flex-end;justify-content:center;background:rgba(20,31,58,.45);animation:fd .18s}
.panel{width:100%;max-width:430px;max-height:88vh;max-height:88svh;background:var(--fondo);border-radius:24px 24px 0 0;display:flex;flex-direction:column;animation:up .24s cubic-bezier(.2,.8,.2,1)}
.sh-h{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;padding:22px 20px 14px;border-bottom:1px solid var(--linea)}
.sh-h::before{content:"";position:absolute;left:50%;transform:translateX(-50%);margin-top:-14px;width:40px;height:4px;border-radius:4px;background:var(--linea)}
.sh-h h2{font:700 24px/1.15 var(--disp);margin:8px 0 0}.x:focus:not(:focus-visible){outline:none}.x{border:0;background:var(--tarjeta);border:1px solid var(--linea);width:38px;height:38px;border-radius:50%;display:grid;place-items:center;cursor:pointer;flex:none}
.sh-b{overflow-y:auto;padding:16px 20px calc(28px + env(safe-area-inset-bottom,0px));-webkit-overflow-scrolling:touch}
.sh-b>p,.blk p{margin:0 0 12px;font-size:14px;line-height:1.55}.blk{margin-top:18px}.blk h4{font:700 18px var(--disp);margin:0 0 10px}
.ul{margin:0;padding-left:18px;display:grid;gap:7px;font-size:14px;line-height:1.5}.ruta{margin:0;padding-left:20px;display:grid;gap:9px;font-size:14px}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}.btns.col{flex-direction:column}.btns.col .btn{justify-content:center}
.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font:600 13px var(--txt);padding:11px 15px;border-radius:99px;border:1px solid var(--linea);background:var(--tarjeta)}
.btn .i{width:16px;height:16px}.btn.solid{background:var(--tinta);color:var(--crema);border-color:var(--tinta)}
.list{padding:4px 16px}.pl{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid var(--linea)}.pl:last-child{border:0}
.pn{min-width:0}.pn b{display:block;font-weight:600;font-size:14px}.pn small{display:block;color:var(--t2);font-size:12px;margin-top:2px}
.pl.star .pn b::after{content:"★";color:var(--ink);margin-left:6px;font-size:11px}
.acts{display:flex;gap:6px;flex:none}.ab{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:var(--chip);color:var(--ink)}.ab .i{width:17px;height:17px}
.tags{display:flex;flex-wrap:wrap;gap:7px}.tags span{padding:7px 11px;border-radius:99px;background:var(--tarjeta);border:1px solid var(--linea);font-size:12.5px;font-weight:600}
.tags.plus{margin-top:8px}.tags.plus span{background:var(--chip);border-color:transparent;color:var(--ink)}
.dots{display:flex;gap:8px;margin-bottom:12px}.dots i{width:28px;height:28px;border-radius:50%;background:color-mix(in srgb,var(--acc) 40%,#fff);display:grid;place-items:center}
.dots i.ok{background:var(--acc)}.dots i.ok::after{content:"";width:9px;height:5px;border-left:2px solid var(--azul);border-bottom:2px solid var(--azul);transform:rotate(-45deg) translate(1px,-1px)}
.toast{position:fixed;left:50%;bottom:96px;transform:translateX(-50%);background:var(--tinta);color:var(--crema);font:600 13px var(--txt);padding:10px 16px;border-radius:99px;opacity:0;transition:.2s;pointer-events:none;z-index:40}.toast.show{opacity:1}
/* modo revisión */
p.rev{display:none}body.rev p.rev{display:block;font-size:11.5px;line-height:1.4;color:#7a4b00;background:#FFF4DC;border:1px dashed #E3B45C;border-radius:12px;padding:8px 11px;margin:0 0 12px}
@keyframes up{from{transform:translateY(40px);opacity:.4}}@keyframes fd{from{opacity:0}}
@media (prefers-reduced-motion:reduce){.panel,.sheet{animation:none}}
"""
JS = r"""
const views=[...document.querySelectorAll('[data-view]')];let openSheet=null;
if(location.search.includes('pendientes'))document.body.classList.add('rev');
function show(id){const s=document.getElementById('sh-'+id);if(!s)return;if(openSheet)openSheet.hidden=true;s.hidden=false;s.querySelector('.sh-b').scrollTop=0;openSheet=s;document.body.classList.add('lock');s.querySelector('.x').focus({preventScroll:true});}
function hide(){if(openSheet){openSheet.hidden=true;openSheet=null;document.body.classList.remove('lock');}}
function go(){const h=decodeURIComponent(location.hash.slice(1))||'portada';const [v,sh]=h.split('/');
 const view=views.find(x=>x.dataset.view===v)||views[0];
 if(document.body.dataset.v!==view.dataset.view){views.forEach(x=>x.hidden=x!==view);document.body.dataset.v=view.dataset.view;window.scrollTo(0,0);}
 document.querySelectorAll('.nav a').forEach(a=>a.classList.toggle('on',a.dataset.v===view.dataset.view));
 if(sh)show(sh);else hide();}
addEventListener('hashchange',go);go();
document.addEventListener('click',ev=>{const t=ev.target.closest('[data-sheet]');
 if(t&&!ev.target.closest('.ab,.btn:not([data-sheet])')){ev.preventDefault();const v=document.body.dataset.v;location.hash=v+'/'+t.dataset.sheet;return;}
 if(ev.target.closest('.x')||ev.target.classList.contains('sheet')){ev.preventDefault();history.length>1?history.back():(location.hash=document.body.dataset.v);}});
addEventListener('keydown',ev=>{if(ev.key==='Escape'&&openSheet)history.back();});
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(b.dataset.copy);}catch(e){}
 const t=document.querySelector('.toast');t.textContent='Copiado: '+b.dataset.copy;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1600);}));
"""

FONTS = os.path.join(W, "_fuente", "fonts")
def local_fonts():
    """Fuentes servidas en local (sin depender de Google al abrir la web: funciona sin conexión y no bloquea el render).
    Descarga una sola vez Philosopher y Montserrat (OFL) a _fuente/fonts/ y devuelve los @font-face."""
    import urllib.request
    css_path = os.path.join(FONTS, "fonts.css")
    if not os.path.exists(css_path):
        os.makedirs(FONTS, exist_ok=True)
        url = "https://fonts.googleapis.com/css2?family=Philosopher:ital,wght@0,700;1,700&family=Montserrat:wght@500;600;700&display=swap"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"})
        css = urllib.request.urlopen(req).read().decode()
        blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face \{.*?\})", css, re.S)
        keep = []
        for subset, blk in blocks:
            if subset not in ("latin", "latin-ext"): continue
            fam = re.search(r"font-family: '([^']+)'", blk).group(1); sty = re.search(r"font-style: (\w+)", blk).group(1); wgt = re.search(r"font-weight: (\d+)", blk).group(1)
            src = re.search(r"url\((https://[^)]+\.woff2)\)", blk).group(1)
            fn = f"{fam.replace(' ', '')}-{wgt}{'i' if sty == 'italic' else ''}-{subset}.woff2"
            if not os.path.exists(os.path.join(FONTS, fn)): open(os.path.join(FONTS, fn), "wb").write(urllib.request.urlopen(src).read())
            keep.append(blk.replace(src, "../assets/fonts/" + fn))
        open(css_path, "w").write("\n".join(keep))
    shutil.copytree(FONTS, os.path.join(OUT, "assets", "fonts"), dirs_exist_ok=True)
    return open(css_path).read()

def build():
    shutil.rmtree(OUT, ignore_errors=True)
    for d in ("assets/fotos", "vms", "vb"): os.makedirs(os.path.join(OUT, d))
    fontcss = local_fonts()
    logo = open(os.path.join(R, "00_BRAND", "LOGOS_SVG", "vms_logo.svg"), encoding="utf-8").read()
    paths = re.findall(r'<path fill-rule="nonzero"[^>]*/>', logo)
    open(os.path.join(OUT, "assets", "vms_mark.svg"), "w", encoding="utf-8").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="254 346 87 118">' + "".join(paths) + "</svg>")
    copy_svg = "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2'><rect x='8' y='8' width='12' height='12' rx='2'/><path d='M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3'/></svg>\")"
    nav = "".join(f'<a href="#{v}" data-v="{v}"><span>{ic(i)}</span>{e(t)}</a>' for v, t, i in NAV)
    page = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<meta name="theme-color" content="#141F3A"><meta name="robots" content="noindex"><title>Villa Mi Sueño · Welcome book</title>'
            '<link rel="icon" href="../assets/vms_mark.svg">'
            f'<style>{fontcss}:root{{--copy:{copy_svg}}}{CSS}</style></head><body><div class="app">'
            + s_portada() + s_inicio() + s_casa() + s_reglas() + s_explora() +
            f'<nav class="nav" aria-label="Secciones">{nav}</nav>{sheets()}<div class="toast" role="status"></div></div><script>{JS}</script></body></html>')
    open(os.path.join(OUT, "vms", "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write('<!doctype html><meta http-equiv="refresh" content="0;url=vms/">')
    vb = os.path.join(W, "sitio", "vb", "index.html")
    if os.path.exists(vb): shutil.copy(vb, os.path.join(OUT, "vb", "index.html"))
    faltan = [s for s in ("portada", "anfitriones", "casa", "piscina", "explora") if not os.path.exists(os.path.join(FOT, s + ".jpg"))]
    print("ok ->", os.path.join(OUT, "vms", "index.html"), "| hojas:", len(SHEETS), "| fotos pendientes:", ", ".join(faltan) or "ninguna")

if __name__ == "__main__":
    build()
