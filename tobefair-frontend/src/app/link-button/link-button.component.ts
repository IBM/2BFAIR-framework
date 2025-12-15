// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component, Input, input } from '@angular/core';

@Component({
  selector: 'app-link-button',
  standalone: true,
  imports: [],
  templateUrl: './link-button.component.html',
  styleUrl: './link-button.component.css'
})
export class LinkButtonComponent {
  @Input() label = "Button Label";
  @Input() url = "";

  redirect() {
    window.location.href = this.url;
  }

}
