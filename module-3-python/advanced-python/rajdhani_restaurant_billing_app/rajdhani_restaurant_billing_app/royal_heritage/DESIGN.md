# Design System Document: Heritage Modernism

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Regal Heritage Editorial."** 

In a fast-paced restaurant environment, software often feels like a utility—cold, mechanical, and cluttered. This design system breaks that template by treating the billing interface as a high-end digital concierge. We move away from the rigid "grid of boxes" and toward a layout that feels like a curated editorial piece. By leveraging intentional asymmetry, overlapping tonal surfaces, and a sophisticated serif-to-sans-serif hierarchy, we reflect the warmth of Indian hospitality and the prestige of the brand.

## 2. Colors: Tonal Depth & Warmth
The palette is rooted in deep maroons and warm golds, balanced by a "Paper White" background that feels more premium than a standard digital white.

### The Palette (Material Design Tokens)
*   **Primary (The Soul):** `primary` (#49000a) and `primary_container` (#6b0f1a). Used for high-emphasis actions and brand moments.
*   **Secondary (The Accent):** `secondary` (#795900) and `secondary_container` (#fdca56). Reserved for status indicators, active states, and "Premium" callouts.
*   **Neutral (The Canvas):** `surface` (#faf9f6) through `surface_container_highest` (#e3e2e0).

### The "No-Line" Rule
To achieve a high-end editorial feel, **1px solid borders are strictly prohibited for sectioning.** 
Boundaries must be defined solely through:
1.  **Background Color Shifts:** Placing a `surface-container-low` component against a `surface` background.
2.  **Vertical White Space:** Using the spacing scale to create mental groupings.
3.  **Soft Shadows:** Extremely diffused ambient light rather than structural lines.

### Signature Textures & Gradients
Main CTAs (like "Complete Payment") should use a subtle linear gradient from `primary` to `primary_container` at a 135-degree angle. This provides a tactile, "silken" feel that flat color cannot replicate. For floating action panels, use **Glassmorphism**: a semi-transparent `surface_container_low` with a 20px backdrop blur to allow the warm background tones to bleed through.

## 3. Typography: The Editorial Balance
We pair the timeless authority of a Serif with the high-performance readability of a modern Sans-Serif.

*   **Display & Headlines (Noto Serif):** Used for guest names, table numbers, and grand totals. This font carries the "Heritage" weight. It should feel like a printed menu heading.
*   **Body & Labels (Plus Jakarta Sans):** Used for dish names, quantities, and technical billing data. It provides the "Modern" efficiency required for a fast-paced environment.
*   **The Hierarchy:** Use `display-md` for the final bill amount. Use `label-md` in `on_surface_variant` (#564241) for "secondary" information like timestamps or waiter IDs.

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are often "dirty." In this design system, we stack surfaces to create hierarchy.

*   **The Layering Principle:** 
    *   **Level 0 (Base):** `surface` (#faf9f6).
    *   **Level 1 (Cards/Tables):** `surface_container_low` (#f4f3f1).
    *   **Level 2 (Active/Focus):** `surface_container_highest` (#e3e2e0).
*   **Ambient Shadows:** For "floating" elements like a checkout modal, use a shadow with a 40px blur, 0px offset, and 6% opacity using the `primary` color (#49000a) as the shadow tint. This creates a warm, natural lift.
*   **The Ghost Border:** If a boundary is required for accessibility (e.g., in a high-glare kitchen environment), use `outline_variant` (#ddc0bf) at **15% opacity**. It should be felt, not seen.

## 5. Components

### Table Cards
*   **Styling:** No borders. Use `surface_container_low`. 
*   **State:** When a table is "Occupied," use a `secondary_container` (#fdca56) accent bar (4px) on the left edge.
*   **Content:** The Table Number uses `headline-lg` (Noto Serif).

### Food Category Chips
*   **Styling:** Use `rounded-full` (9999px) with `surface_container_high` (#e9e8e5).
*   **Active State:** Transition to `primary` (#49000a) with `on_primary` (#ffffff) text.
*   **Interaction:** Subtle scale-down (98%) on press to simulate tactile feedback.

### Billing Statements (The Editorial Invoice)
*   **Header:** Use `headline-sm` for the restaurant branch name.
*   **Itemized List:** Strictly no dividers. Use `body-md` for item names. Use `title-sm` (bold) for prices to ensure they are the first thing the eye catches.
*   **The "Grand Total" Block:** Use `surface_container_highest`. Apply a `xl` (0.75rem) corner radius. The price must be in `display-sm` (Noto Serif) using the `primary` color.

### Buttons
*   **Primary:** Gradient of `primary` to `primary_container`. Text in `label-md` (All Caps, letter-spacing: 0.05em).
*   **Secondary:** `surface_container_highest` with `on_surface` text. No border.
*   **Tertiary:** Transparent background. Use `primary` color for text with a `sm` (0.125rem) gold underline (`secondary`).

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical margins (e.g., a wider left margin for titles) to create an editorial feel.
*   **Do** use `notoSerif` for any currency symbol ($ or ₹) to maintain the premium brand voice.
*   **Do** ensure high contrast for the "Print Bill" and "Pay" actions—these should always use the `primary` brand color.

### Don't:
*   **Don't** use pure black (#000000). Use `tertiary` (#2c1c0f) for deep shadows or text that needs to feel heavy but warm.
*   **Don't** use standard "Material Design" cards with 100% opaque borders.
*   **Don't** crowd the interface. If the bill is long, use "Surface Nesting" (scrolling inside a `surface_container_low` area) rather than cluttering the main `surface`.