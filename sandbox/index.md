---
layout: default
title: "Sandbox"
permalink: /sandbox/
sitemap: false
robots: noindex
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>UPI & Cyber Sovereignty Infographic</title>

  <!-- React + Babel -->
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

  <!-- Tailwind -->
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

  <!-- Lucide React (browser build) -->
  <script src="https://unpkg.com/lucide-react/dist/lucide-react.min.js"></script>

  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body class="bg-gray-900 text-white">

  <div id="root"></div>

  <script type="text/babel">

    const {
      Shield,
      Layers,
      AlertTriangle,
      TrendingUp,
      Lock,
      Users,
      Database,
      Network
    } = lucideReact;

    function UPIInfographic() {
      return (
        <div className="w-full bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 text-white p-8 font-sans">

          <div className="max-w-6xl mx-auto">

            {/* HEADER */}
            <div className="text-center mb-12">
              <div className="inline-block bg-gradient-to-r from-blue-500 to-purple-600 px-6 py-2 rounded-full mb-4">
                <h1 className="text-3xl font-bold">UPI & Cyber Sovereignty</h1>
              </div>
              <p className="text-blue-200 text-lg">
                Critical Insights from Sunil Abraham's ORF Analysis (July 2020)
              </p>
              <p className="text-sm text-blue-300 mt-2">
                Beyond the Success Story: Governance Gaps & Strategic Tensions
              </p>
            </div>

            {/* PARADOX */}
            <div className="bg-gradient-to-r from-red-900/40 to-orange-900/40 border-2 border-red-500 rounded-xl p-6 mb-8">
              <div className="flex items-start gap-4">
                <AlertTriangle className="w-12 h-12 text-red-400 flex-shrink-0 mt-1"/>
                <div>
                  <h2 className="text-2xl font-bold mb-3 text-red-200">The Central Paradox</h2>
                  <p className="text-lg leading-relaxed">
                    Despite creating a world-class payment infrastructure to prevent foreign control,
                    <span className="font-bold text-yellow-300">
                      {" "}Google Pay and Walmart's PhonePe dominate 80%+ of the market{" "}
                    </span>
                    by 2020. BHIM’s share collapsed from 45% (2016) to 5.37% (2020).
                    The sovereignty tool became a foreign gateway.
                  </p>
                </div>
              </div>
            </div>

            {/* STRATEGIC FAILURES */}
            <div className="grid md:grid-cols-2 gap-6 mb-8">

              {/* NPCI Identity Crisis */}
              <div className="bg-slate-800/60 backdrop-blur border border-blue-500/30 rounded-xl p-6">
                <div className="flex items-center gap-3 mb-4">
                  <Layers className="w-8 h-8 text-blue-400"/>
                  <h3 className="text-xl font-bold">NPCI's Identity Crisis</h3>
                </div>
                <div className="space-y-3 text-sm">
                  <p className="bg-slate-700/50 p-3 rounded border-l-4 border-purple-500">
                    <span className="font-semibold text-purple-300">Multiple Hats Problem:</span>
                    {" "}NPCI acts as competitor (BHIM), platform provider, regulator, rule-maker, and judge.
                  </p>
                  <p className="bg-slate-700/50 p-3 rounded border-l-4 border-red-500">
                    <span className="font-semibold text-red-300">Critical Error:</span>
                    {" "}BHIM was proprietary instead of a BSD-licensed FOSS reference implementation.
                  </p>
                  <p className="text-gray-300 italic">
                    This enabled accusations of preferential treatment and weakened local innovation.
                  </p>
                </div>
              </div>

              {/* Open Washing */}
              <div className="bg-slate-800/60 backdrop-blur border border-orange-500/30 rounded-xl p-6">
                <div className="flex items-center gap-3 mb-4">
                  <Lock className="w-8 h-8 text-orange-400"/>
                  <h3 className="text-xl font-bold">"Open Washing" Deception</h3>
                </div>
                <div className="space-y-3 text-sm">
                  <p className="bg-slate-700/50 p-3 rounded border-l-4 border-yellow-500">
                    <span className="font-semibold text-yellow-300">Rhetoric vs Reality:</span>
                    {" "}UPI promoted as “open” but specifications remain proprietary.
                  </p>
                  <p className="bg-slate-700/50 p-3 rounded border-l-4 border-orange-500">
                    <span className="font-semibold text-orange-300">Security by Obscurity:</span>
                    {" "}UPI 2.0 addressed vulnerabilities but did not publish updated standards.
                  </p>
                  <p className="text-gray-300 italic">
                    Violates India’s own FOSS policies and undermines digital sovereignty.
                  </p>
                </div>
              </div>

            </div>

            {/* INDIA STACK */}
            <div className="bg-gradient-to-r from-purple-900/40 to-blue-900/40 border border-purple-500/30 rounded-xl p-6 mb-8">
              <div className="flex items-center gap-3 mb-4">
                <Database className="w-8 h-8 text-purple-400"/>
                <h2 className="text-2xl font-bold">India Stack: Coupled Vulnerabilities</h2>
              </div>

              <div className="grid md:grid-cols-4 gap-4">

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="text-purple-400 font-bold mb-2">Layer 1: Presenceless</div>
                  <div className="text-xs text-gray-300">
                    Aadhaar biometric ID — <span className="text-red-400">No tokenization increases fraud risk</span>
                  </div>
                </div>

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="text-blue-400 font-bold mb-2">Layer 2: Paperless</div>
                  <div className="text-xs text-gray-300">
                    eKYC, eSign, DigiLocker — <span className="text-red-400">Key escrow + biometric dependency</span>
                  </div>
                </div>

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="text-green-400 font-bold mb-2">Layer 3: Cashless</div>
                  <div className="text-xs text-gray-300">
                    UPI — <span className="text-yellow-400">Works without Aadhaar but interlinked risks accumulate</span>
                  </div>
                </div>

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="text-orange-400 font-bold mb-2">Layer 4: Consent</div>
                  <div className="text-xs text-gray-300">
                    DEPA — <span className="text-yellow-400">Account aggregators lack incentives</span>
                  </div>
                </div>

              </div>

              <p className="mt-4 text-sm text-gray-300 bg-red-900/30 p-3 rounded border-l-4 border-red-500">
                <span className="font-semibold">BHIM Data Leak (June 2020):</span>
                {" "}7 million users’ Aadhaar numbers, device fingerprints, and bank details exposed — non-replaceable identifiers mean permanent consequences.
              </p>
            </div>

            {/* SURVEILLANCE */}
            <div className="bg-slate-800/60 backdrop-blur border border-cyan-500/30 rounded-xl p-6 mb-8">
              <div className="flex items-center gap-3 mb-4">
                <Network className="w-8 h-8 text-cyan-400"/>
                <h2 className="text-2xl font-bold">360° Financial Surveillance</h2>
              </div>

              <div className="grid md:grid-cols-2 gap-4">

                <div>
                  <h4 className="font-semibold text-cyan-300 mb-2">NPCI Visibility Includes:</h4>
                  <ul className="text-sm text-gray-300 space-y-1">
                    <li>• Aadhaar numbers</li>
                    <li>• Device fingerprints (IMEI, DeviceID)</li>
                    <li>• IP + GPS metadata</li>
                    <li>• All bank account numbers</li>
                    <li>• Full transaction graphs</li>
                  </ul>
                </div>

                <div>
                  <h4 className="font-semibold text-red-300 mb-2">Privacy Trade-off</h4>
                  <p className="text-sm text-gray-300">
                    Earlier IMPS used Mobile Money Identifiers — NPCI had <span className="font-semibold text-green-400">no account visibility</span>.  
                    UPI makes surveillance far easier.
                  </p>
                  <p className="text-xs mt-2 text-yellow-300 bg-yellow-900/20 p-2 rounded">
                    Without tokenization + strong privacy law, UPI enables unprecedented financial profiling.
                  </p>
                </div>

              </div>
            </div>

            {/* REFORMS */}
            <div className="bg-gradient-to-r from-green-900/40 to-teal-900/40 border border-green-500/30 rounded-xl p-6 mb-8">

              <div className="flex items-center gap-3 mb-4">
                <Shield className="w-8 h-8 text-green-400"/>
                <h2 className="text-2xl font-bold">Abraham's Critical Reforms</h2>
              </div>

              <div className="grid md:grid-cols-3 gap-4 text-sm text-gray-300">

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="font-bold text-green-300 mb-2">Governance</div>
                  <ul className="space-y-2">
                    <li>→ Co-regulatory model</li>
                    <li>→ NPCI must not compete with PSPs</li>
                    <li>→ Transparent approvals</li>
                    <li>→ Public performance dashboards</li>
                  </ul>
                </div>

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="font-bold text-blue-300 mb-2">Technical Openness</div>
                  <ul className="space-y-2">
                    <li>→ Multistakeholder standards (W3C/IETF)</li>
                    <li>→ Publish UPI specifications</li>
                    <li>→ FOSS reference apps</li>
                    <li>→ Mandatory tokenization</li>
                  </ul>
                </div>

                <div className="bg-slate-800/60 p-4 rounded">
                  <div className="font-bold text-purple-300 mb-2">Market Competition</div>
                  <ul className="space-y-2">
                    <li>→ Sustainable MDR regime</li>
                    <li>→ Encourage NUE competitors</li>
                    <li>→ User-funded account aggregators</li>
                    <li>→ Consider Mojaloop federation</li>
                  </ul>
                </div>

              </div>
            </div>

            {/* HISTORICAL PARALLEL */}
            <div className="bg-slate-800/60 backdrop-blur border border-blue-500/30 rounded-xl p-6 mb-8">
              <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
                <TrendingUp className="w-6 h-6 text-blue-400"/>
                The 1914 British Parallel
              </h2>
              <p className="text-sm text-gray-300 leading-relaxed">
                Britain attempted to “derange Germany’s national economy” by controlling global communication hubs.
                It failed because cable surveillance had character limits.
                Today the problem is reversed:
                <span className="font-semibold text-red-300"> surveillance is trivial</span>,
                but
                <span className="font-semibold text-yellow-300"> sovereignty remains elusive without governance reform</span>.
              </p>
            </div>

            {/* BOTTOM LINE */}
            <div className="bg-gradient-to-r from-yellow-900/40 to-orange-900/40 border-2 border-yellow-500 rounded-xl p-6">
              <div className="flex items-start gap-4">
                <Users className="w-10 h-10 text-yellow-400 flex-shrink-0 mt-1"/>
                <div>
                  <h2 className="text-2xl font-bold mb-3 text-yellow-200">The Strategic Lesson</h2>
                  <p className="text-base leading-relaxed mb-3">
                    <span className="font-bold text-white">1.34B transactions, $35B monthly (June 2020)</span> —
                    UPI succeeded at scale. But Abraham argues sovereignty requires more than infrastructure:
                    it needs governance clarity, open standards, privacy safeguards, and sustainable incentives.
                  </p>
                  <p className="text-sm text-gray-300 bg-black/30 p-4 rounded border-l-4 border-orange-500">
                    <span className="font-semibold text-orange-300">For other nations:</span>
                    State-led payment networks work, but design choices determine whether sovereignty is achieved or outsourced.
                  </p>
                </div>
              </div>
            </div>

            {/* FOOTER */}
            <div className="mt-8 text-center text-sm text-blue-300">
              <p>Source: Sunil Abraham, “Unified Payment Interface: Towards Greater Cyber Sovereignty”</p>
              <p>ORF Issue Brief No. 380, July 2020</p>
            </div>

          </div>
        </div>
      );
    }

    ReactDOM.render(<UPIInfographic />, document.getElementById("root"));

  </script>
</body>
</html>

</script>
