#!/usr/bin/env python3
import sys, json

# NOTE: this is a completely vibecoded script to trim asciinema casts.

def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def main():
    if len(sys.argv) < 4:
        print("Usage: trim_cast.py input.cast output.cast OFFSET [START]", file=sys.stderr)
        sys.exit(1)

    inp = sys.argv[1]
    outp = sys.argv[2]
    offset = float(sys.argv[3])
    start = float(sys.argv[4]) if len(sys.argv) >= 5 else None

    with open(inp, "r", encoding="utf-8") as f:
        text = f.read()

    # Try single JSON array first
    try:
        data = json.loads(text)
        if isinstance(data, list) and len(data) >= 2:
            header = data[0]
            events = data[1:]
            new_events = []
            for ev in events:
                ts = float(ev[0])
                if start is not None and ts < start:
                    continue
                new_ts = ts - offset
                if new_ts < 0:
                    new_ts = 0.0
                ev[0] = new_ts
                new_events.append(ev)
            out_data = [header] + new_events
            with open(outp, "w", encoding="utf-8") as out:
                json.dump(out_data, out, separators=(",", ":"))
            return
    except Exception:
        pass

    # Fallback: JSON Lines (header on first line, then [ts,"type",payload] per line)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    header = json.loads(lines[0])
    new_lines = [json.dumps(header, separators=(",", ":"))]

    for ln in lines[1:]:
        ev = json.loads(ln)
        ts = float(ev[0])
        if start is not None and ts < start:
            continue
        new_ts = ts - offset
        if new_ts < 0:
            new_ts = 0.0
        ev[0] = new_ts
        new_lines.append(json.dumps(ev, separators=(",", ":")))

    with open(outp, "w", encoding="utf-8") as out:
        out.write("\n".join(new_lines) + "\n")

if __name__ == "__main__":
    main()
