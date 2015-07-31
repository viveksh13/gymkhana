from flask import Flask, render_template, redirect, request

from binascii import hexlify, unhexlify
from markdown2 import markdown


from glob import glob
from binascii import hexlify, unhexlify

societies = {
    "res": "Research Society",
    "spo": "Sports Society",
    "lit": "Literary Society",
    "tec": "Technical Society",
    "cul": "Cultural Society",
    "aca": "Academic Society",
    "gen": "Student Gymkhana",
    "nss": "NSS IIT-Mandi",
    
}

months = [
    "-", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

def get_entries_raw():
    return glob("posts/*")

def get_entries(filter_soc="", filter_clb=""):
    """Collect entries from /posts.
    Entries in posts are named yyyymmdd.soc.clb.md"""
    entries_raw = get_entries_raw()
    entries = []

    # We need the latest entries to be displayed first.
    for entry_raw in reversed(sorted(entries_raw)):

        # Collect meta-data from filename of entry.
        date, society, club = get_entry_mdata(entry_raw)
        if filter_soc != "" and filter_soc != society:
            continue
        if filter_clb != "" and filter_clb != club:
            continue

        with open(entry_raw) as doc:
            entries.append([hexlify(entry_raw),
                            doc.readline(),
                            societies[society],
                            date])

    return entries


def get_date(entry_raw):
    date_raw = entry_raw[6:14]
    year, month, day = date_raw[:4], months[int(date_raw[4:6])], date_raw[6:8]
    return month + " " + day + ", " + year

def get_society(entry_raw):
    return entry_raw[15:18]

def get_club(entry_raw):
    return entry_raw[19:22]

def get_entry_mdata(entry_raw):
    return [get_date(entry_raw), get_society(entry_raw), get_club(entry_raw)]


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    entries = get_entries()
    return render_template("home.html", entries=entries)

#TECHSOC
@app.route("/tech")
def tech():
    entries = get_entries(filter_soc="tec")
    return render_template("tech.html", entries=entries)

@app.route("/tech/info")
def tech_info():
    return render_template("tech_info.html")


@app.route("/techevents")
def techevents():
    return render_template("techevents.html")

@app.route("/rob")
def robotics():
    entries = get_entries(filter_clb="rob")
    return render_template("rob.html", entries=entries)

@app.route("/ele")
def electronics():
    entries = get_entries(filter_clb="rob")
    return render_template("ele.html", entries=entries)

@app.route("/pro")
def programming():
    entries = get_entries(filter_clb="pro")
    return render_template("pro.html", entries=entries)

@app.route("/mad")
def mad():
    entries = get_entries(filter_clb="mad")
    return render_template("mad.html", entries=entries)

@app.route("/stac")
def stac():
    entries = get_entries(filter_clb="stac")
    return render_template("stac.html", entries=entries)

@app.route("/ene")
def energy():
    entries = get_entries(filter_clb="ene")
    return render_template("ene.html", entries=entries)

@app.route("/scri")
def scri():
    entries = get_entries(filter_clb="scri")
    return render_template("scri.html", entries=entries)


#litsoc

@app.route("/lit")
def literary():
    entries = get_entries(filter_soc="lit")
    return render_template("literary.html", entries=entries)

@app.route("/lit/info")
def literary_info():
    return render_template("literary_info.html")

@app.route("/edl")
def edls():
    entries = get_entries(filter_clb="edl")
    return render_template("edl.html", entries=entries)

@app.route("/mag")
def magazine():
    entries = get_entries(filter_clb="mag")
    return render_template("mag.html", entries=entries)




#cultsoc
@app.route("/cult")
def cultural():
    entries = get_entries(filter_soc="cul")
    return render_template("cult.html", entries=entries)

@app.route("/cult/info")
def cult_info():
    return render_template("cult_info.html")

@app.route("/mus")
def music():
    entries = get_entries(filter_clb="mus")
    return render_template("mus.html", entries=entries)

@app.route("/dan")
def dance():
    entries = get_entries(filter_clb="dan")
    return render_template("dan.html", entries=entries)

@app.route("/dra")
def drama():
    entries = get_entries(filter_clb="dra")
    return render_template("dra.html", entries=entries)

@app.route("/pho")
def photography():
    entries = get_entries(filter_clb="pho")
    return render_template("pho.html", entries=entries)

@app.route("/pm")
def pm():
    entries = get_entries(filter_clb="pm")
    return render_template("pm.html", entries=entries)

@app.route("/cultevents")
def cultevents():
    return render_template("cultevents.html")


@app.route("/art")
def art():
    entries = get_entries(filter_clb="art")
    return render_template("art.html", entries=entries)


#sports
@app.route("/sports")
def sports():
    entries = get_entries(filter_soc="spo")
    return render_template("sports.html", entries=entries)

@app.route("/sports/info")
def sports_info():
    return render_template("sports_info.html")


@app.route("/cri")
def cricket():
    entries = get_entries(filter_clb="cri")
    return render_template("cri.html", entries=entries)

@app.route("/foo")
def football():
    entries = get_entries(filter_clb="foo")
    return render_template("foo.html", entries=entries)

@app.route("/bas")
def basketball():
    entries = get_entries(filter_clb="bas")
    return render_template("bas.html", entries=entries)

@app.route("/bad")
def badminton():
    entries = get_entries(filter_clb="bad")
    return render_template("bad.html", entries=entries)

@app.route("/tt")
def tt():
    entries = get_entries(filter_clb="tt")
    return render_template("tt.html", entries=entries)

@app.route("/vol")
def volleyball():
    entries = get_entries(filter_clb="vol")
    return render_template("vol.html", entries=entries)

@app.route("/hoc")
def hockey():
    entries = get_entries(filter_clb="hoc")
    return render_template("hoc.html", entries=entries)


@app.route("/ath")
def athletics():
    entries = get_entries(filter_clb="ath")
    return render_template("ath.html", entries=entries)

@app.route("/sportsevents")
def sportsevents():
    return render_template("sportsevents.html")

#acad           
@app.route("/acad")
def academics():
    entries = get_entries(filter_soc="aca")
    return render_template("acad.html", entries=entries)

@app.route("/acad/info")
def acad_info():
    return render_template("acad_info.html")

#nss
@app.route("/nss")
def nss():
    entries = get_entries(filter_soc="nss")
    return render_template("nss.html", entries=entries)


@app.route("/nss/info")
def nss_info():
    return render_template("nss_info.html")



@app.route("/nso")
def nso():
    return render_template("nso_info.html")


@app.route("/contacts")
def contacts():
    
    return render_template("contacts.html")

@app.route("/gallery")
def gallery():
    
    return render_template("gallery.html")

@app.route("/lounge")
def lounge():
    return render_template("lounge.html")

@app.route("/loungec")
def loungec():
    return render_template("loungec.html")





@app.route("/hk/")
def hk():
    return render_template("hk_info.html")


@app.route("/entry")
def entry():
    entry_hex = request.args.get("id")
    entry_raw = unhexlify(entry_hex)

    entries_raw = get_entries_raw()
    entries = get_entries()
    if entry_raw in entries_raw:
        date, society, club = get_entry_mdata(entry_raw)
        with open(entry_raw) as doc:
            entry = [markdown(doc.read()), societies[society], date]

        print(entry)

        return render_template("entry.html",
                               entry=entry,
                               recent_entries=entries[:4])

    else:
        return "Problem with retrieving entry."






if __name__ == '__main__':
    app.run()
