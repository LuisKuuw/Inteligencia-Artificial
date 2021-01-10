def Generate_image(filenames, local_filenames=None, tblfile='readme.htm'):
    global local_files
    local_files = local_filenames or filenames
    summary_table = {}
    for f in filenames:
        fulltext = '\n'.join(map(string.rstrip, open(f).readlines()))
        text = fulltext
        for (pattern, repl) in replacements:
            text = re.sub(pattern, repl, text)
        text = '<<header("AIMA Python file: %s")>><pre>%s</pre><<footer>>' % (
            f, text)
        open(f[:-3]+'.htm', 'w').write(text)
        if tblfile:
            ch = find1(r'Chapters?\s+([^ \)"]*)', fulltext)
            module = f.replace('.py','')
            lines = fulltext.count('\n')
            desc = find1(r'"""(.*)\n', fulltext).replace('"""', '')
            summary_table.setdefault(ch,[]).append((module, lines, desc))
    if tblfile:
        totallines = 0
        tbl = ["<tr><th>Chapter<th>Module<th>Files<th>Lines<th>Description"]
        fmt = "<tr><td align=right>%s<th>%s<td>%s<td align=right>%s<td>%s"
        items = summary_table.items(); items.sort(num_cmp)
        for (ch, entries) in items:
            for (module, lines, desc) in entries:
                totallines += lines
                files = link(module+'.py', '.py')
                if os.path.exists(module+'.txt'):
                    files += ' ' + link(module+'.txt', '.txt')
                tbl += [fmt % (ch, link(module+'.html', module),
                               files, lines, desc)]
        tbl += [fmt % ('', '', '', totallines, ''), "</table>"]
        old = open(tblfile).read()
        new = re.sub("(?s)(<table border=1>)(.*)(</table>)",
                     r'\1' + '\n'.join(tbl) + r'\3', old, 1)
        open(tblfile, 'w').write(new)