from events import load_events

def main():
    events = load_events()

    print("=" * 50)
    print("ANGELS ONLINE EVENT NOTIFIER")
    print("=" * 50)
    print()

    print(f"Eventos carregados: {len(events)}")
    print()

    for event in events:
        print(
            f'{event["id"]} | {event["name"]} | Dia {event["day"]} | '
            f'{event["summer_time"]} / {event["winter_time"]}'
        )


if __name__ == "__main__":
    main()