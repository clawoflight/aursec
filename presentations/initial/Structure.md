# Initial Präsentation
## Inhalt dieser Datei

- Einleitung
- Inhalt
- Was ist die AUR
- Sicherheitsprobleme der AUR
- Begriffserklärung: Blockchain
- Unser Projekt
- Zeitplan

## Einleitung

    Initial-Präsentation Piater Bennett - Krismer Lukas

Liebe Anwesende,
(kurze Vorstellung ). Wir wollen ihnen nun unser Thema näherbringen.

    A blockchain approach to securing software packages of the AUR

Klingt vielleicht für den ein oder anderen kompliziert, aber nach dieser Präsentation sollten Sie einen groben Überblick haben, was wir genau machen.

## Inhalt

- Was ist die AUR
- Sicherheitsprobleme der AUR
- Begriffserklärung: Blockchain
- Unser Projekt
- Zeitplan

## Was ist die AUR

    AUR = Arch User Repository
    __TODO:__ Add Info to AUR

Die AUR ist die User-Repository von Arch Linux. Auf diese können alle Paketbuilts stellen. Das heißt jeder kann Programme zur Verfügung stellen. Dies vereinfacht die Installation von vielen Programmen enorm. Zum Beispiel sind alle Programme von JetBrain (IntelliJ, PyCharm, ...) in dieser Repo. Allerdings gibt es bei dieser Art von Repo auch Sicherheitsprobleme

## Sicherheitsprobleme der AUR

    Threat-Diagramm

Die Angriffsmöglichkeiten sind breit gefächert:
__TODO:__ Alle Angriffsmöglichkeiten kurz erklären

## Begriffserklärung: Blockchain

    Blockchain = Verteilte Datenbank
    enthält erweiterbare Listen von Datensätzen
    gesichert durch Prüfsumme des vorherigen Datensatzes
    Verwendet vor allem bei Kryptowährung

Eine Blockchain ist eine verteilte Datenbank die erweiterbare Listen von Datensätzen enthält. Die Integrität wird durch die Prüfsumme des voherigen Datensatzes gesichert. Das wohl bekannteste Beispiel ist die Transaktionsicherung der Kryptowährung Bitcoin.

    Beispiel auf der Tafel oder als Bild siehe http://bit.ly/2e2IvzL (nicht für uns nutzbar)

## unser Projekt
### Behebung von Sicherheitslücken

    Threatdiagramm

__TODO:__ Welche Probleme werden gelöst welche nicht

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

__TODO:__ Teile erklären

### Verwendete Technologien

- Ethereum
- JSON
- Python ?? 
- yaourt ....

__TODO:__ Formulierung


## Zeitplan

    25.10 Prototyp hashing                                         [B]
    25.10 od. 01.11 Initialpräsentation                            [L]
    15.11 Prototyp Bibliothek ohne Blockchain-backend              [B/L?]
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

__TODO:__ Formulierung
