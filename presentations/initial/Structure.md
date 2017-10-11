# Initial Präsentation
## Inhalt dieser Datei

- Einleitung
- Inhalt
- Was ist die AUR
- Unser Projekt
- Zeitplan

## Einleitung

    Initial-Präsentation Piater Bennett - Krismer Lukas

Liebe Anwesende,
Mein Name ist Lukas, und Bennett und ich werden euch heute unser Bachelorarbeitsthema näherbringen. Da oben steht so eine schöne große Überschrift ... 

    Aursec - A blockchain approach to securing software packages

Und wir möchten heute ein bisschen darauf eingehen wie man Softwarepakete, in unserem Fall von der AUR, sicherer machen kann.
Am Anfang werden wir auf die AUR und ihre Probleme eingehen und später zeigen wir dann, wie wir Teilprobleme mithilfe einer Blockchain lösen wollen. Zum Schluss schauen wir uns dann noch unser Zeitmanagement und unsere Verantwortlichkeiten an.

## Inhalt

- Was ist die AUR
- Sicherheitsprobleme der AUR
- Unser Projekt
- Zeitplan

## Was ist die AUR

    AUR = Arch User Repository


## Sicherheitsprobleme der AUR

    Threat-Diagramm

Die Angriffsmöglichkeiten sind breit gefächert:


## unser Projekt
### Behebung von Sicherheitslücken

    Threatdiagramm


### Begriffserklärung: Blockchain

    Blockchain = Verteilte Datenbank
    enthält erweiterbare Listen von Datensätzen
    gesichert durch Prüfsumme des vorherigen Datensatzes
    Verwendet vor allem bei Kryptowährung

Eine Blockchain ist eine verteilte Datenbank die erweiterbare Listen von Datensätzen enthält. Die Integrität wird durch die Prüfsumme des voherigen Datensatzes gesichert. Das wohl bekannteste Beispiel ist die Transaktionsicherung der Kryptowährung Bitcoin.

    Beispiel auf der Tafel oder als Bild siehe http://bit.ly/2e2IvzL (nicht für uns nutzbar)

### Workflow

    Blockchain 1 Block für jeden Build
    enthält Package namen und Hash
    Prüfung des Hashes durch Vergleich mit Blockchain

Unser Programm schaltet sich ein sobald ein neues Paket gebaut wird. Als erstes wird ein Hash berechnet, welcher dann, mittels des Namens des Paketes, mit dem dezeit gültigen Hash des Packetes in der Blockchain verglichen wird. Falls es sich um einen gültigen Hash handelt, wird der Hash automatisch der Blockchain hinzugefügt. Falls es sich um einen ungültigen Hash handelt oder der Hash noch unsicher ist (gewisse Anzahl die konfiguriert werden kann) wird in einen manuellen Modus geschalten, in dem man die Installation abbrechen oder fortführen kann. Falls fortgeführt wird, wird der neue Hash in der Blockchain abgelegt. (Somit können sich mit der Zeit die Hashes von Paketen ändern.)

### Teile

- Programm für Ethereum
- Bibliothek
- Arch-Paket
- Web- oder CLI-Interface
- Integration


### Verwendete Technologien

- Ethereum
- JSON
- Python ?? 
- yaourt ....



## Zeitplan

    25.10 Prototyp hashing                                         [B]
    08.11 Initialpräsentation                                      [L]
    15.11 Prototyp Bibliothek ohne Blockchain-backend              [B/L]
    15.11 Bash-API für Blockchain ohne Implementierung             [L]
    30.11 Solidity-Programm vorerst fertig                         [B]
    08.12 Einheitliche lokale Blockchain für Entwicklungszwecke    [L]
    08.12 Lauffähiger Server mit Ethereum-node?                    [B/L]
    15.12 Backend der Bibliothek                                   [L]
    20.12 contrib: Rudimentäre pre-build-hooks in aurutils         [B]
    10.01 contrib: TLS-public-key-pinning in aurutils              [B]
    10.01 Konfiguration und Trust-cutoff                           [L]
    15.01 Testweise Integration in aurutils                        [B]
    15.02 Arch-Paket inkl. privater Blockchain                     [B]
    01.03 Fertigstellung von Bibliothek und aurutils-Hook          [B]
    01.04 Web- oder CLI-Interface                                  [L]
    15.04 Erste Fassung des Papers 
    ??.05 Abgabe des Papers
    ??.05 Abschlusspräsentation                                    [L]

