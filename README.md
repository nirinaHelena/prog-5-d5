# ☕ Coffee Machine System

Une simulation modulaire et orientée objet d'une machine à café automatique en Java, permettant aux utilisateurs de payer, choisir un café, et recevoir leur boisson.

---

## Statut

**En développement** – Ce projet est en phase de prototypage. Certaines fonctionnalités peuvent changer ou être incomplètes.

---

## Fonctionnalités

- **Paiement**
  - Jeton ou paiement numérique
  - Timeout si aucun café n’est sélectionné dans un délai imparti
- **Sélection de café**
  - Liste dynamique des cafés disponibles selon le stock
  - Validation de la sélection
- **Distribution**
  - Préparation de la boisson si toutes les conditions sont remplies
  - Vérification : eau, lumière, parfum disponible
- **Gestion des erreurs**
  - Timeout, choix indisponible, rupture de stock, panne pendant la préparation

---

## Cas d'utilisation

1. **Payer le café** – L’utilisateur insère un jeton ou paie numériquement.
2. **Choisir le café** – Il sélectionne une boisson dans une liste.
3. **Recevoir le café** – Si tout est en ordre, le café est préparé et distribué.

---

## Exceptions possibles

| Exception                    | Description |
|-----------------------------|-------------|
| `JetonTimeoutException`     | Aucun café sélectionné après paiement dans un temps limite |
| `ChoiceNotAvailableException` | Café choisi inexistant ou désactivé |
| `OutOfStockException`       | Stock épuisé pour le café demandé |
| `MachineInterruptedException` | Interruption pendant la préparation (plus d'eau, lumière coupée, etc.) |

---

## Structure orientée objet

- `CoffeeMachine` – Point d'entrée principal du système
- `PaymentProcessor` – Gestion et validation du paiement
- `CoffeeSelector` – Affichage et sélection des cafés disponibles
- `CoffeeDispenser` – Préparation de la boisson
- `Coffee` – Modèle de données pour un café
- `ExceptionHandler` – Gestion des exceptions

---

## Démarrage du projet

### Prérequis

- Java 8+
- Un terminal ou IDE (ex: IntelliJ, Eclipse)

### Compilation et exécution

```bash
javac *.java
java CoffeeMachineApp
