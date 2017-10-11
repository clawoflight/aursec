# AUR

## Issues (3m)
    \begin{itemize}
    	\item lokale Ausführung von \texttt{PKGBUILDS} -- \texttt{.install}
    	\item keine Vertrauensketten/Signaturen von PKGBUILDS
    	\item Zu viel und einfacher Zugang zu Paketen --> Server-seitige Signaturen würden auch nur MITM verhindern
    	\item Keine Prüfsummen von VCS-Quellen
	\end{itemize}

2 Angriffszenarios:

	\begin{itemize}
		\item Manipulierung von VCS-Quellen
		\item Manipulierung von Paketquellen
	\end{itemize}

===> grundlegende Probleme ohne drastische Änderung der AUR unlösbar,
vertrauenswürdige Prüfsummen nötig --> Point of Trust, Vetting/Auditing

ABER: Dezentrale Datenbank kann drumherum aufgebaut werden und schützt zumindest gegen gezielte Angriffe!

# What we do

## demo (~2m + Lukas)
- Installation/update von AUR-Paketen mit aurutils+aursec
	+ Normaler workflow
	+ VCS-Pakete
- Pipeline-Bestandteile einzeln zeigen, evtl. mit `-v`/`-d`?
- TUI

TODO: Befehle aufschreiben, die wir dann verwenden können.
Wollen wir die Demo mit asciinema aufnehmen, um sie schneller zeigen zu können?

# How we do it

## Workflow (3m)

// TODO

Workflow for each package as seen in state machine:

- generate ID and Hash (executing in firejail sandbox)
- query & compare
- = & >: continue, committing hash to chain
- = & <=: prompt
- !=: prompt
- exit 0 or != 0


## Components (~2m + Lukas)
UNIX philosophy - small tools doing one thing well.
Work on stdin/stdout with blocking I/O.

Pipeline:

- aursec (state machine)
- aursec-hash (generate ID and hash)
- aursec-verify-hashes (blockchain interaction)

--> Good parallelism, straightforward to maintain and extend

# Comparison with other approaches (2m)
Nachteile Blockchain:

- Lokale Kopie --> Speicher
- Hintergrundsynchronisation --> Bandbreite, Internetverbindung
- Hohe Mining-schwierigkeit --> Sehr hohe Rechenleistung

Alternativen:

- Zentrale Datenbank (Single Point of {Trust,Failure})
- Sichere Repo Downstream von AUR (Aufwand, Single Point of Trust)
	--> Für spezielle Zwecke oder geschlossene Organisationen sicherlich sinnvoll, wird auch gemacht!
- Re-Design der AUR (und Ablehnung ihrer Designkriterien - wird nicht passieren)

# Thinks we learned (~1m + Lukas)
- Solidity
	+ Half-way between C and JS
	+ Associative arrays
	+ Fairly high-level to use
- Bash
	+ Arcane syntax and many pitfalls
	+ Very productive: high-level and easy integration
	+ **Think in streams!**
	+ **Use Shellcheck** (Written in Haskell!)

# Outlook (?)

# Timetable (?)
