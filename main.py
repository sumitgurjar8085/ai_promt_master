"""
AI Prompt Master - Python Flet UI & App Logic (main.py)
Cross-platform mobile-friendly app (~390px x ~740px) with gamified token economy,
streak tracking, prompt unlocking, clipboard integration, and prompt engineering guide.
"""

import flet as ft
from app_data import APP_SETTINGS, AI_COURSE_GUIDE, PROMPTS_DATABASE


def main(page: ft.Page):
    # Page setup & Theme
    page.title = APP_SETTINGS["app_title"]
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = APP_SETTINGS["window_width"]
    page.window_height = APP_SETTINGS["window_height"]
    page.window_resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    page.bgcolor = "#0B0E14"

    # State variables with client storage persistence
    current_tokens = (
        page.client_storage.get("user_tokens")
        if page.client_storage.contains_key("user_tokens")
        else APP_SETTINGS["initial_tokens"]
    )
    daily_streak = (
        page.client_storage.get("daily_streak")
        if page.client_storage.contains_key("daily_streak")
        else 1
    )
    daily_bonus_claimed = (
        page.client_storage.get("daily_bonus_claimed")
        if page.client_storage.contains_key("daily_bonus_claimed")
        else False
    )
    unlocked_prompt_ids = (
        set(page.client_storage.get("unlocked_prompts"))
        if page.client_storage.contains_key("unlocked_prompts")
        else set()
    )

    def save_state():
        page.client_storage.set("user_tokens", current_tokens)
        page.client_storage.set("daily_streak", daily_streak)
        page.client_storage.set("daily_bonus_claimed", daily_bonus_claimed)
        page.client_storage.set("unlocked_prompts", list(unlocked_prompt_ids))

    # App bar / Header components
    streak_chip = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("🔥", size=18),
                ft.Text(f"Day {daily_streak}", size=15, weight=ft.FontWeight.W_600, color="#FF9800"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=4,
        ),
        bgcolor="#1C1814",
        border=ft.border.all(1, "#3A2814"),
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=12, vertical=6),
    )

    tokens_chip = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("🪙", size=18),
                ft.Text(f"{current_tokens} Tokens", size=15, weight=ft.FontWeight.BOLD, color="#FFD54F"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=4,
        ),
        bgcolor="#1F1D13",
        border=ft.border.all(1, "#4E3E14"),
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=14, vertical=6),
    )

    def show_snackbar(message: str, is_error: bool = False):
        sb = ft.SnackBar(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.icons.ERROR_OUTLINE if is_error else ft.icons.CHECK_CIRCLE_OUTLINE,
                        color="#FF5252" if is_error else "#4CAF50",
                    ),
                    ft.Text(message, color=ft.colors.WHITE, size=13, weight=ft.FontWeight.W_500),
                ],
                spacing=8,
            ),
            bgcolor="#1E222D" if not is_error else "#2A1517",
            open=True,
            duration=3500,
        )
        page.overlay.append(sb)
        page.update()

    def update_header_stats():
        streak_text: ft.Text = streak_chip.content.controls[1]
        streak_text.value = f"Day {daily_streak}"
        tokens_text: ft.Text = tokens_chip.content.controls[1]
        tokens_text.value = f"{current_tokens} Tokens"
        page.update()

    def on_claim_daily_bonus(e):
        nonlocal current_tokens, daily_bonus_claimed
        if not daily_bonus_claimed:
            current_tokens += APP_SETTINGS["daily_bonus"]
            daily_bonus_claimed = True
            claim_bonus_btn.disabled = True
            claim_bonus_btn.text = "Bonus Claimed ✓"
            claim_bonus_btn.icon = ft.icons.CHECK_CIRCLE
            claim_bonus_btn.style = ft.ButtonStyle(color=ft.colors.GREY_500, bgcolor="#1A1E26")
            save_state()
            update_header_stats()
            show_snackbar(f"🎉 Claimed daily streak reward! +{APP_SETTINGS['daily_bonus']} Tokens added!")

    def on_watch_ad(e):
        nonlocal current_tokens
        # Rewarded system simulation
        current_tokens += APP_SETTINGS["ad_reward"]
        save_state()
        update_header_stats()
        show_snackbar(f"🎬 Rewarded Ad watched! +{APP_SETTINGS['ad_reward']} Tokens credited to balance!")

    def on_unlock_and_copy(prompt_data):
        nonlocal current_tokens
        pid = prompt_data["id"]
        cost = prompt_data["token_cost"]
        full_prompt = prompt_data["full_prompt"]
        title = prompt_data["title"]

        if pid in unlocked_prompt_ids:
            # Already unlocked: Free copy
            page.set_clipboard(full_prompt)
            show_snackbar(f"📋 '{title}' copied to clipboard!")
            return

        if current_tokens >= cost:
            current_tokens -= cost
            unlocked_prompt_ids.add(pid)
            save_state()
            update_header_stats()
            page.set_clipboard(full_prompt)
            # Re-render cards to reflect unlocked badge
            refresh_prompt_cards()
            show_snackbar(f"✨ Unlocked '{title}' (-{cost} Tokens) & copied to clipboard!")
        else:
            show_snackbar(
                f"⚠️ Insufficient tokens! You need {cost} tokens (have {current_tokens}). Tap 'Watch Short Ad' to earn +15!",
                is_error=True,
            )

    # Action Buttons
    claim_bonus_btn = ft.ElevatedButton(
        text=f"Claim Daily Bonus (+{APP_SETTINGS['daily_bonus']} 🪙)",
        icon=ft.icons.LOCAL_FIRE_DEPARTMENT,
        icon_color="#FF9800",
        color=ft.colors.WHITE,
        bgcolor="#241B10",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "#E65100"),
        ),
        on_click=on_claim_daily_bonus,
    )

    watch_ad_btn = ft.ElevatedButton(
        text=f"Watch Short Ad (+{APP_SETTINGS['ad_reward']} 🪙)",
        icon=ft.icons.PLAY_CIRCLE_FILL,
        icon_color="#2196F3",
        color=ft.colors.WHITE,
        bgcolor="#101928",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "#1976D2"),
        ),
        on_click=on_watch_ad,
    )

    # Prompt Cards List Container
    prompts_column = ft.Column(spacing=12, scroll=ft.ScrollMode.AUTO)

    def create_prompt_card(p):
        pid = p["id"]
        is_unlocked = pid in unlocked_prompt_ids
        cost = p["token_cost"]

        btn = ft.ElevatedButton(
            text="Copy Full Prompt" if is_unlocked else f"Unlock & Copy ({cost} 🪙)",
            icon=ft.icons.CONTENT_COPY if is_unlocked else ft.icons.LOCK_OPEN,
            color=ft.colors.WHITE,
            bgcolor="#1E3A8A" if not is_unlocked else "#065F46",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            on_click=lambda _: on_unlock_and_copy(p),
        )

        badge_row = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(p["category"], size=11, weight=ft.FontWeight.W_600, color="#90CAF9"),
                    bgcolor="#132338",
                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    border_radius=6,
                ),
                ft.Container(
                    content=ft.Text(
                        "UNLOCKED" if is_unlocked else f"{cost} TOKENS",
                        size=11,
                        weight=ft.FontWeight.BOLD,
                        color="#81C784" if is_unlocked else "#FFD54F",
                    ),
                    bgcolor="#1B3320" if is_unlocked else "#2E2412",
                    padding=ft.padding.symmetric(horizontal=8, vertical=4),
                    border_radius=6,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        return ft.Container(
            content=ft.Column(
                controls=[
                    badge_row,
                    ft.Text(p["title"], size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Text(p["desc"], size=13, color="#94A3B8"),
                    ft.Divider(height=1, color="#202938"),
                    ft.Row([btn], alignment=ft.MainAxisAlignment.END),
                ],
                spacing=8,
            ),
            bgcolor="#161B26",
            border=ft.border.all(1, "#232D3F"),
            border_radius=12,
            padding=16,
        )

    def refresh_prompt_cards():
        prompts_column.controls.clear()
        for p in PROMPTS_DATABASE:
            prompts_column.controls.append(create_prompt_card(p))
        page.update()

    refresh_prompt_cards()

    # Prompt Engineering Guide Dialog
    def open_course_guide(e):
        guide_items = []
        for ch in AI_COURSE_GUIDE:
            guide_items.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                [
                                    ft.Text(f"Chapter {ch['chapter']}: {ch['title']}", size=14, weight=ft.FontWeight.BOLD, color="#90CAF9"),
                                    ft.Container(
                                        content=ft.Text(ch["tag"], size=10, color="#FFB74D", weight=ft.FontWeight.W_600),
                                        bgcolor="#332414",
                                        padding=ft.padding.symmetric(horizontal=6, vertical=2),
                                        border_radius=4,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Text(ch["summary"], size=12, italic=True, color="#CBD5E1"),
                            ft.Text(ch["content"], size=12, color="#94A3B8"),
                        ],
                        spacing=6,
                    ),
                    bgcolor="#111724",
                    border=ft.border.all(1, "#1E293B"),
                    border_radius=8,
                    padding=10,
                )
            )

        dialog = ft.AlertDialog(
            title=ft.Text("📘 AI Prompt Engineering Guide", size=16, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column(guide_items, scroll=ft.ScrollMode.AUTO, spacing=10),
                width=350,
                height=420,
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda _: page.close(dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            bgcolor="#161B26",
        )
        page.open(dialog)

    # Header Card
    header_view = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Row(
                            [
                                ft.Text("⚡", size=22),
                                ft.Text("AI Prompt Master", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                            ],
                            spacing=6,
                        ),
                        ft.IconButton(
                            icon=ft.icons.MENU_BOOK,
                            icon_color="#90CAF9",
                            tooltip="AI Course Guide (3 Chapters)",
                            on_click=open_course_guide,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[streak_chip, tokens_chip],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
                ft.Row(
                    controls=[claim_bonus_btn, watch_ad_btn],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    wrap=True,
                ),
            ],
            spacing=14,
        ),
        bgcolor="#121722",
        border=ft.border.all(1, "#1E2738"),
        border_radius=16,
        padding=16,
        margin=ft.margin.only(left=12, right=12, top=12, bottom=8),
    )

    # Main layout container
    main_layout = ft.Container(
        width=390,
        content=ft.Column(
            controls=[
                header_view,
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text("Master Prompts Catalog", size=15, weight=ft.FontWeight.BOLD, color="#E2E8F0"),
                            ft.Text(f"{len(PROMPTS_DATABASE)} Templates", size=12, color="#64748B"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    padding=ft.padding.symmetric(horizontal=16, vertical=4),
                ),
                ft.Container(
                    content=prompts_column,
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=12),
                ),
            ],
            expand=True,
            spacing=4,
        ),
        expand=True,
    )

    page.add(main_layout)


if __name__ == "__main__":
    ft.app(target=main)
