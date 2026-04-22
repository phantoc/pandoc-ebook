-- index.lua: A simple pandoc filter to handle indexing
-- For PDF (LaTeX), it keeps \index{...} as is.
-- For other formats, it can collect them (though generating a real index with page numbers for HTML/EPUB is complex)

local index_entries = {}

function RawInline (el)
  if el.format == "tex" and el.text:match("\\index{.*}") then
    if FORMAT == "latex" then
      return el
    else
      -- For non-latex, we might want to collect these or just hide them
      -- Realistically, HTML/EPUB don't have "page numbers".
      -- We could turn them into anchors or just remove them to avoid clutter.
      return {} 
    end
  end
end

-- If the user wants an Index section at the end for non-PDFs, 
-- we would need a more complex filter that tracks locations.
-- For now, let's focus on enabling it for PDF and keeping it clean for others.
